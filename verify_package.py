"""Verify the release checksum and reproduce the archived study (Python 3.10+)."""
from pathlib import Path
import hashlib
import subprocess
import sys
import tempfile
import zipfile

root = Path(__file__).resolve().parent
archive = root / 'replication-package.zip'
hashes = dict(line.strip().split(maxsplit=1)[::-1]
              for line in (root / 'SHA256SUMS').read_text().splitlines() if line.strip())
actual = hashlib.sha256(archive.read_bytes()).hexdigest()
if actual != hashes[archive.name]:
    raise SystemExit('Replication archive checksum mismatch.')
with tempfile.TemporaryDirectory(prefix='bn-replication-') as directory:
    destination = Path(directory).resolve()
    with zipfile.ZipFile(archive) as source:
        for member in source.infolist():
            target = (destination / member.filename).resolve()
            if not target.is_relative_to(destination):
                raise SystemExit('Unsafe archive member path.')
        source.extractall(destination)
    subprocess.run([sys.executable,
                    str(destination / 'replication-package/scripts/reproduce.py'),
                    '--output-dir', str(root / 'results')], check=True)
print('Release archive checksum and numerical reproduction: PASS')
