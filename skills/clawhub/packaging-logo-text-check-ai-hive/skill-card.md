## Description:

Helps packaging design, ecommerce operations, brand review, and AI image teams compare packaging references with supplied or generated media to identify differences in layout, logo use, text, barcode areas, net content, and claims.

This skill is ready for commercial/non-commercial use.

## Publisher:

[wubin1836](https://clawhub.ai/user/wubin1836)

### License/Terms of Use:

MIT-0

## Use Case:

External packaging, ecommerce, brand, and AI content teams use this skill to turn packaging logo and text accuracy checks into a structured review workflow with issue lists, evidence screenshots or timecodes, risk levels, repair suggestions, and recheck records. Developers may also use its bundled scripts to create project blueprints, call AI-HIVE generation APIs, upload authorized media, poll tasks, download outputs, and run deterministic ffmpeg video edits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security summary says the skill packages broad AI-HIVE media generation, upload, billing, and credential setup behind a packaging-checking identity.

Mitigation: Install it only when remote AI-HIVE media generation is intended; review final prompts, routing, budget, and task parameters before running generation commands.

Risk: The security guidance says selected media may be uploaded to remote services and outputs may be downloaded to a chosen local directory.

Mitigation: Use only authorized media, avoid sensitive or regulated content unless allowed by policy, and confirm output directories before execution.

Risk: The security guidance says the skill expects an AI-HIVE API key and may store local configuration when initialized.

Mitigation: Provide credentials through environment variables or protected local config, keep placeholder keys in examples, and remove or rotate any accidentally exposed key.

Risk: The artifact states OCR may miss issues and legal, barcode, ingredient, production, and claim information requires professional review.

Mitigation: Treat model output as a review aid, mark uncertain facts as unverified, and retain human final review for regulated packaging and brand claims.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/wubin1836/skills/packaging-logo-text-check-ai-hive)
- [AI-HIVE web app](https://ai-hive.iclip.cn/chat)
- [AI-HIVE OpenAPI base URL](https://ai-hive.iclip.cn/api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with runnable command examples and optional JSON task or blueprint records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include AI-HIVE routing choices, model or price snapshots, task IDs, local output paths, and review records when generation tasks are used.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
