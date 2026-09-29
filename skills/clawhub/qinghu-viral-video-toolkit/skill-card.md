## Description:

Analyzes short-video links to derive viral-style scripts, generate adapted marketing videos through qhkit, and extract audio from returned video URLs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

External creators, sellers, and agent operators use this skill to analyze reference short videos, adapt the resulting script for their own product, generate a new marketing video, or extract audio when they have appropriate rights to the source media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on an external qhkit npm package and may change the local execution environment during setup.

Mitigation: Review the package before installation, prefer platform-managed or pinned installs where possible, and verify downloaded runtime archives before use.

Risk: Using qhkit requires an API token that may be stored locally or supplied through the environment.

Mitigation: Use least-privilege token handling, avoid exposing the token in prompts or logs, and prefer environment or platform secret management when available.

Risk: Provided media or links may be uploaded to or processed by the Qinghu service and video generation may consume account credits.

Mitigation: Confirm the user has rights to the source material, disclose credit estimates before generation when available, and avoid audio or video replication for unauthorized commercial use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/autoagc/skills/qinghu-viral-video-toolkit)
- [@iqinghu/qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)
- [Qinghu API key dashboard](https://www.iqinghu.com/workbench/dashboard/api-keys?urlCode=1788417429126)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands, JSON command arguments, task identifiers, generated media URLs, extracted audio file paths, and credit usage notes]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May rely on qhkit CLI JSON responses and ffmpeg output; video generation may require polling before final media URLs are available.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
