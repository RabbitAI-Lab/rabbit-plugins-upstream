## Description:

Provides a Guandata BI agent layer that routes standard BI work to official CLI components and guides ETL governance, SmartETL rewrites, custom charts, v7 publishing, SuperApp workflows, and AI-native ADS design.

This skill is ready for commercial/non-commercial use.

## Publisher:

[maojiebc](https://clawhub.ai/user/maojiebc)

### License/Terms of Use:

MIT

## Use Case:

Developers, data engineers, and BI operators use this skill to work with Guandata BI environments, especially when standard official CLI flows need additional governance judgment, compatibility handling, or implementation playbooks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide destructive or state-changing BI operations, including DELETE, force, publish, and data replacement workflows.

Mitigation: Use only with explicit authorization, least-privilege BI credentials, dry-run or preview steps where available, and explicit confirmation before irreversible actions.

Risk: Mutable installation paths such as global npm installs and GitHub npx execution can change dependencies or retrieved source over time.

Mitigation: Pin and review dependencies and source revisions before installation, and inspect SKILL.md, scripts, and dependencies before use.

Risk: Reference files and troubleshooting workflows may involve raw BI errors, payloads, tokens, cookies, or customer data if users paste operational details into the skill.

Mitigation: Do not persist secrets, cookies, raw customer data, or sensitive payloads in skill reference files; redact operational logs before adding them to documentation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/maojiebc/skills/guanyuan-majia)
- [Project homepage](https://github.com/maojiebc/majia-guanyuan)
- [Official CLI compatibility notes](references/official-cli-compatibility.md)
- [SmartETL full-chain rewrite playbook](references/part-b17-fullchain-rewrite.md)
- [Custom chart playbook](references/custom-chart-playbook.md)
- [HTML dashboard playbook](references/part-c-html-dashboard.md)
- [v7 page and card publishing pipeline](references/v7-page-card-publish-pipeline.md)
- [SuperApp pipeline](references/part-e-superapp-pipeline.md)
- [AI-native ADS design](references/ai-native-ads-design.md)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, shell commands, configuration]

**Output Format:** [Markdown guidance with command examples, JSON payload guidance, and code snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include operational checks, dry-run steps, and review requirements before BI write actions.]

## Skill Version(s):

3.1.11 (source: SKILL.md metadata, package.json, manifest.json, CHANGELOG, released 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
