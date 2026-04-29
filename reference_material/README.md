# Reference Material

Add your product-specific documentation here before running the test case generator prompt.

The AI prompt reads these files to understand your product's domain, features, and terminology before generating test cases.

---

## Folder Guide

### `product_info/`
Place high-level product context here. Examples:
- Product overview document
- Feature summary or capability list
- Glossary of domain terms
- Architecture overview (non-confidential)

### `user_guides/`
Place user-facing documentation here. Examples:
- User manuals (PDF or Markdown)
- Help center articles
- Onboarding guides
- Release notes

### `requirements/`
Place feature specs and tickets here. Examples:
- Product Requirement Documents (PRDs)
- Jira/Linear ticket exports
- Acceptance criteria documents
- API specifications (OpenAPI/Swagger)

### `ui_screenshots/`
Place UI screenshots here to give the AI visual context. Examples:
- Screenshots of the feature under test
- Annotated UI flows
- Error state screenshots

---

## Tips

- The more relevant context you provide, the more accurate and domain-specific the generated test cases will be.
- You do not need to fill every folder — add only what is available and relevant.
- After adding files, update the file paths at the top of `prompts/test_case_generator.prompt` to match.
- Do not commit confidential or proprietary documents to a public repository.
