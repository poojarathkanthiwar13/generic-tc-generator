# Generic Test Case Generator

A structured, AI-assisted framework for generating high-quality test cases for any software product. Bring your own reference material — prompts, templates, and testing resources are ready to use out of the box.

## How It Works

This toolkit uses a two-step workflow:

1. **Add your reference material** — Drop your product docs, user guides, and requirements into the `reference_material/` folders.
2. **Run the generation prompt** — Open `prompts/test_case_generator.prompt` in your AI assistant (Claude, ChatGPT, etc.), point it at your reference material, and paste in the requirement you want to test.

The AI reads your reference material first, then generates structured test cases in a CSV format.

---

## Project Structure

```
generic-tc-generator/
├── prompts/
│   ├── test_case_generator.prompt     # Main AI prompt for generating test cases
│   └── document_generator.prompt     # AI prompt for writing feature documentation
├── resources/
│   ├── testing_principles.txt         # The 7 Principles of Software Testing
│   ├── test_case_writing_techniques.txt  # 13 test design techniques (BVA, EP, etc.)
│   └── image_generator.py             # Utility to generate test images (JPG/PNG/HEIC)
├── templates/
│   ├── test_plan_template.md          # Reusable test plan structure
│   └── sample_testcase_format.csv    # TestMo-compatible CSV format reference
├── reference_material/                # ← Add YOUR product docs here
│   ├── product_info/                  # Product overview, feature summaries
│   ├── user_guides/                   # User manuals, guides, PDFs
│   ├── requirements/                  # PRDs, feature specs, tickets
│   └── ui_screenshots/                # UI screenshots for context
└── generated_test_cases/              # Output folder — generated CSVs go here
```

---

## Quick Start

### Step 1 — Add your reference material

Place your files in the appropriate `reference_material/` subfolder:

| Folder | What to put here |
|---|---|
| `product_info/` | Product overviews, feature summaries, domain context |
| `user_guides/` | User manuals, help docs, onboarding guides |
| `requirements/` | PRDs, Jira tickets, feature specs, acceptance criteria |
| `ui_screenshots/` | Screenshots that show the UI being tested |

### Step 2 — Open the generation prompt

Open `prompts/test_case_generator.prompt` in your AI assistant. At the top of the prompt, update the file paths to point to your actual reference material files.

### Step 3 — Paste your requirement

At the bottom of the prompt (under `## Requirements`), paste the feature description, ticket, or PRD section you want test cases for.

### Step 4 — Save the output

Save the generated CSV to `generated_test_cases/` for your records.

---

## Output Format

Test cases are output as CSV compatible with [TestMo](https://testmo.com/). Each row contains:

| Column | Description |
|---|---|
| `Case ID` | Sequential number |
| `Case` | Concise, action-oriented title |
| `Precondition` | Setup state required before test execution |
| `Execution Steps` | Numbered plain-text steps |
| `Expected Result` | Numbered list of verifiable outcomes |
| `Priority` | High / Normal / Low |
| `Component` | Product area or feature being tested |

See `templates/sample_testcase_format.csv` for a complete column reference.

---

## Testing Principles & Techniques

The `resources/` folder includes two foundational references:

- **testing_principles.txt** — The 7 Principles of Software Testing (ISTQB standard)
- **test_case_writing_techniques.txt** — 13 techniques including BVA, EP, Decision Tables, State Transitions, and more

The generation prompt automatically applies these to every requirement.

---

## Document Generation

Use `prompts/document_generator.prompt` to turn your generated test cases into user-facing feature documentation. Paste in your feature description and test cases — the prompt produces structured docs with Overview, Prerequisites, How It Works, Key Behaviors, Error Handling, and Related Topics sections.

---

## Test Image Generation

`resources/image_generator.py` generates random test images in JPG, JPEG, PNG, and HEIC formats — useful for testing file upload features.

**Requirements**: `pip install Pillow numpy pillow-heif`

**Usage**:
```bash
python resources/image_generator.py
```

---

## Contributing

1. Fork this repository
2. Add your improvements to prompts, templates, or resources
3. Submit a pull request

---

## License

MIT
