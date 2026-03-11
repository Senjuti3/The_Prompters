@echo off
echo ========================================
echo Evaluation Software - Setup and Run
echo ========================================
echo.

echo Step 1: Installing required packages...
pip install -r requirements.txt
echo.

echo Step 2: Running evaluation software...
echo.
python evaluation_software.py

pause
