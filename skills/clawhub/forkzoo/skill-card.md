## Description: <br>
ForkZoo helps agents adopt and manage GitHub-native digital pets that evolve through scheduled AI-powered workflows. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[levi-law](https://clawhub.ai/user/levi-law) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and agent users use ForkZoo to adopt monkey, cat, dog, or lion pets, check pet status and evolution, trigger interactions, and view community pet galleries. The skill guides GitHub-based setup and operation for a forked pet repository. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill asks for GitHub access that can create forks, enable Actions, and configure public GitHub Pages. <br>
Mitigation: Use a dedicated fine-grained or temporary GitHub token limited to the intended pet repository where possible. <br>
Risk: Adopted repositories may run workflows and publish public pages automatically. <br>
Mitigation: Inspect the forkZoo repositories and workflows before adoption, and disable Actions or Pages if the automation is not wanted. <br>
Risk: Long-lived credentials can continue to authorize repository operations after setup. <br>
Mitigation: Revoke the token or delete the fork when the pet automation is no longer needed. <br>


## Reference(s): <br>
- [ForkZoo skill page](https://clawhub.ai/levi-law/skills/forkzoo) <br>
- [ForkZoo main site](https://forkzoo.com) <br>
- [ForkZoo GitHub organization](https://github.com/forkZoo) <br>
- [Original forkMonkey project](https://github.com/roeiba/forkMonkey) <br>
- [ForkZoo gallery](https://forkzoo.com/gallery) <br>
- [ForkZoo leaderboard](https://forkzoo.com/leaderboard) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance] <br>
**Output Format:** [Markdown with inline bash code blocks and command output guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May execute shell scripts that call GitHub APIs when the user provides a GitHub token.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
