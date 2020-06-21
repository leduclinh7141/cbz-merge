@echo off
python cbz-split-folder.py "C:\fmd_1.3.3.0_x86_64-win64\downloads"
python cbz-merge-folder.py -d "C:\fmd_1.3.3.0_x86_64-win64\downloads"
pause