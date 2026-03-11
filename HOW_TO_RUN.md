# How to Run the Evaluation Software

## Quick Start (Easiest Method)

1. **Double-click** `run_evaluation.bat` file
   - This will automatically install dependencies and run the software

## Manual Method

### Step 1: Install Dependencies

Open PowerShell or Command Prompt in this folder and run:

```bash
pip install -r requirements.txt
```

**Note**: If you get permission errors, try:
```bash
pip install --user -r requirements.txt
```

Or run PowerShell/Command Prompt as Administrator.

### Step 2: Prepare Your Files

1. **Place reference images** in this folder:
   - `image1.jpg` (for question 1)
   - `image2.jpg` (for question 2)
   - ... up to `image10.jpg` (for question 10)

   OR update the paths in `config.json`

2. **Have your Excel files ready** from Google Forms:
   - One Excel file per question (10 files total)
   - Each should have Team Number and Image Link columns

### Step 3: Run the Software

**Option A: Interactive Mode (Recommended)**
```bash
python evaluation_software.py
```

Then follow the prompts:
- Enter section number (1 or 2)
- Provide path to each Excel file when asked
- Enter output filename (or press Enter for default)

**Option B: Command Line Mode**
```bash
python evaluation_software.py 1 "question1.xlsx" "question2.xlsx" "question3.xlsx" "question4.xlsx" "question5.xlsx" "question6.xlsx" "question7.xlsx" "question8.xlsx" "question9.xlsx" "question10.xlsx"
```

Replace `1` with `2` for section 2, and replace the Excel filenames with your actual file paths.

## Troubleshooting

### "Module not found" errors
- Make sure you installed dependencies: `pip install -r requirements.txt`
- Try: `pip install --user -r requirements.txt`

### "Permission denied" errors
- Run PowerShell/Command Prompt as Administrator
- Or use: `pip install --user -r requirements.txt`

### "Reference image not found"
- Check that your reference images exist
- Update paths in `config.json` if images are in different locations

### "Could not download image"
- Ensure Google Drive links are shareable (set to "Anyone with the link can view")
- Check your internet connection

## Example Workflow

1. Download 10 Excel files from Google Forms to this folder
2. Place reference images (image1.jpg to image10.jpg) in this folder
3. Run: `python evaluation_software.py`
4. Enter: `1` (for section 1)
5. When prompted, enter paths like:
   - `question1.xlsx`
   - `question2.xlsx`
   - ... (for all 10 files)
6. Press Enter for default output filename
7. Find results in `results_section1.xlsx`

## Output

The software will create an Excel file (e.g., `results_section1.xlsx`) with:
- Team_Number column (sorted 1-200 or 201-400)
- Q1_Score through Q10_Score columns
- Total_Score column

Teams that didn't submit will have 0.0 for that question.
