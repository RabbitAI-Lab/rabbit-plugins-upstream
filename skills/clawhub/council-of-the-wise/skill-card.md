## Description: <br>
Send an idea to the Council of the Wise for multi-perspective feedback using auto-discovered agent personas. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[jeffaf](https://clawhub.ai/user/jeffaf) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
External users and developers use Council to stress-test ideas, project plans, content strategies, and major decisions through multiple expert perspectives, then receive a synthesized verdict with action items and confidence. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: User-provided ideas or documents are sent through a spawned model sub-agent. <br>
Mitigation: Use the skill only with content appropriate for the active model session and avoid sensitive material unless that session is approved for it. <br>
Risk: Custom Markdown files added to the agents folder become future council-member instructions. <br>
Mitigation: Review custom agent files before use and scan them as part of release or installation review. <br>


## Reference(s): <br>
- [Council on ClawHub](https://clawhub.ai/jeffaf/skills/council-of-the-wise) <br>
- [Publisher profile](https://clawhub.ai/user/jeffaf) <br>
- [Daniel Miessler](https://danielmiessler.com/) <br>


## Skill Output: <br>
**Output Type(s):** [analysis, markdown, guidance] <br>
**Output Format:** [Markdown report with synthesis, expert-perspective sections, prioritized action items, and a confidence signal] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May spawn follow-up sub-agents for deeper analysis from one council member; normal review can take 2-5 minutes.] <br>

## Skill Version(s): <br>
1.4.0 (source: server release metadata, frontmatter, changelog released 2026-02-23) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
