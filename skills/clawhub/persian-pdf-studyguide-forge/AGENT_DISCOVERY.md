# Agent discovery card — Persian PDF StudyGuide Forge v1.3.0

## Use when

- The operator supplies or authorizes a Persian/mixed RTL educational PDF.
- The requested output is an offline accessible HTML study guide.
- Fidelity, source-page evidence, large-document resume, AI-assisted proofreading, quizzes or maximum study enrichment are required.

## Do not use when

- The source is unauthorized, access controls would need bypassing, or the requested task is unrelated to educational PDF conversion.
- The environment cannot safely store sensitive source material.
- The operator demands a verbatim guarantee without rendered-page adjudication.

## Decision procedure

1. Confirm authorization and workspace scope.
2. Run `scripts/preflight.py`.
3. Read `SKILL.md` and `docs/WORKFLOW_PLAYBOOK.md`.
4. Choose local-only extraction/build or explicitly approved provider-assisted correction.
5. Treat detected sessions as candidates until reviewed.
6. Run fidelity and QA gates before presenting or packaging.

## Network rule

No network by default. AI provider keys are never bundled. Network requires explicit operator approval and a local provider config that contains environment-variable names rather than values.
