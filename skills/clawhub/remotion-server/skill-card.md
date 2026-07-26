## Description: <br>
Headless video rendering with Remotion v5 on Linux servers, with templates for chat demos, promo videos, title cards, and other Remotion projects. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[mvanhorn](https://clawhub.ai/user/mvanhorn) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use this skill to set up headless Linux video rendering and scaffold Remotion projects for chat demos, promo videos, title cards, and rendered video assets. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Setup can install system browser dependencies and may invoke sudo on supported Linux distributions. <br>
Mitigation: Run setup only on a Linux machine where local package installation is acceptable, and review any sudo prompt before continuing. <br>
Risk: Project creation downloads npm dependencies and writes a local Remotion project. <br>
Mitigation: Create projects in a trusted workspace and review generated files and dependency changes before rendering or publishing. <br>
Risk: Generated templates may contain placeholder demo data or broad example content that is not ready for publication. <br>
Mitigation: Review and replace generated content before publishing rendered videos. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/mvanhorn/skills/remotion-server) <br>
- [Remotion documentation](https://remotion.dev) <br>
- [Remotion Linux dependencies](https://www.remotion.dev/docs/miscellaneous/linux-dependencies) <br>


## Skill Output: <br>
**Output Type(s):** [code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with bash commands and generated TypeScript/JSON project files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scaffolds local Remotion projects and can guide rendering to MP4, WebM, GIF, or PNG sequences through Remotion CLI commands.] <br>

## Skill Version(s): <br>
1.2.1 (source: ClawHub release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
