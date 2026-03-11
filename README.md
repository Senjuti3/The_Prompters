# Evaluation Software - Team Image Accuracy Scoring

This software processes Excel files collected from Google Forms and scores team submissions based on image accuracy comparison.

## Features

- ✅ Processes Excel files from Google Forms
- ✅ Compares submitted images with reference images
- ✅ Scores accuracy using Structural Similarity Index (SSIM)
- ✅ Handles missing submissions (assigns 0 score)
- ✅ Supports two sections (Section 1: Teams 1-200, Section 2: Teams 201-400)
- ✅ Processes 10 questions and combines all scores
- ✅ Generates final Excel output with all scores

## Installation

1. Install Python 3.8 or higher
2. Install required packages:
```bash
pip install -r requirements.txt
```

## Setup

1. **Prepare Reference Images**: Place your reference images (image1.jpg, image2.jpg, ..., image10.jpg) in the same directory as the script, or update paths in `config.json`

2. **Configure Settings**: Edit `config.json` to customize:
   - Section ranges (default: Section 1 = 1-200, Section 2 = 201-400)
   - Reference image paths for each question
   - Column names (if different from default)

## Usage

### Interactive Mode (Recommended)

Simply run:
```bash
python evaluation_software.py
```

The software will prompt you for:
- Section number (1 or 2)
- Paths to 10 Excel files (one per question)
- Output file name

### Command Line Mode

```bash
python evaluation_software.py <section> <excel1> <excel2> ... <excel10>
```

Example:
```bash
python evaluation_software.py 1 question1.xlsx question2.xlsx question3.xlsx question4.xlsx question5.xlsx question6.xlsx question7.xlsx question8.xlsx question9.xlsx question10.xlsx
```

## Excel File Format

Each Excel file from Google Forms should contain:
- **Team Number** column (or similar)
- **Image Link** column (Google Drive shareable links)

The software will automatically detect these columns (case-insensitive).

## Output

The software generates an Excel file with:
- Team Number (sorted 1-200 or 201-400)
- Q1_Score through Q10_Score (one column per question)
- Total_Score (sum of all question scores)

Teams that didn't submit will have a score of 0.0 for that question.

## Configuration File (config.json)

```json
{
    "section1_range": [1, 200],
    "section2_range": [201, 400],
    "reference_images": {
        "question1": "image1.jpg",
        "question2": "image2.jpg",
        ...
    },
    "team_number_column": "Team Number",
    "image_link_column": "Image Link"
}
```

### Changing Reference Images

To use different reference images for a question, update the path in `config.json`:
```json
"question1": "path/to/your/reference_image.jpg"
```

### Changing Section Ranges

To change team number ranges:
```json
"section1_range": [1, 200],  // Teams 1 to 200
"section2_range": [201, 400]  // Teams 201 to 400
```

## How It Works

1. **Read Excel Files**: Reads each Excel file from Google Forms
2. **Extract Data**: Extracts team numbers and image links
3. **Download Images**: Downloads images from Google Drive links
4. **Compare Images**: Compares each submitted image with the reference image using SSIM
5. **Score**: Assigns a similarity score (0-1) for each submission
6. **Handle Missing**: Teams that didn't submit get a score of 0
7. **Combine Results**: Merges all 10 question scores into one Excel file

## Notes

- Google Drive links should be shareable links (with "Anyone with the link can view" permission)
- The software automatically converts Google Drive shareable links to direct download links
- Image comparison uses Structural Similarity Index (SSIM) which is robust to minor variations
- Processing time depends on number of teams and image download speeds
- Missing teams are automatically filled with score 0.0

## Troubleshooting

**Issue**: "Reference image not found"
- Solution: Check that reference images exist at the paths specified in config.json

**Issue**: "Could not download image"
- Solution: Ensure Google Drive links are shareable and have "Anyone with the link can view" permission

**Issue**: "Could not find required columns"
- Solution: Check Excel file format. The software looks for columns containing "team" and "number" (team number) and "image" and "link" (image link)

## Example Workflow

1. Collect 10 Excel files from Google Forms (one per question)
2. Place reference images (image1.jpg to image10.jpg) in the project folder
3. Run: `python evaluation_software.py`
4. Enter section number (1 or 2)
5. Provide paths to 10 Excel files when prompted
6. Get results in `results_section1.xlsx` or `results_section2.xlsx`
