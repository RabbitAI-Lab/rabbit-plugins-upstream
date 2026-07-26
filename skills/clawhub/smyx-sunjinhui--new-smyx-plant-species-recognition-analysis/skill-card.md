## Description: <br>
Accurately identifies plant species from images using cloud-backed computer vision and returns structured information such as species name, family, growth habits, maintenance tips, report details, and report links. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[smyx-sunjinhui](https://clawhub.ai/user/smyx-sunjinhui) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, gardeners, educators, and ecological field workers use this skill to identify plants from images or video and receive structured plant knowledge and report links. Agents can also query cloud-hosted history for prior plant recognition reports associated with the current identity. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Plant media and account-linked identifiers are sent to the publisher's cloud service. <br>
Mitigation: Use only with media approved for third-party cloud processing, and avoid submitting sensitive or regulated images unless the publisher's terms and data handling are acceptable. <br>
Risk: The skill can silently create or reuse an identity and persist local tokens in the workspace. <br>
Mitigation: Run it in an isolated workspace, restrict access to workspace storage, and clear local identity or token data after use when persistence is not desired. <br>
Risk: History lookup can retrieve prior report records associated with the current identity. <br>
Mitigation: Limit use to users authorized to view that report history, and review returned records before sharing them outside the intended audience. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/smyx-sunjinhui/skills/new-smyx-plant-species-recognition-analysis) <br>
- [Publisher Profile](https://clawhub.ai/user/smyx-sunjinhui) <br>
- [Skill Demo](https://lifeemergence.com/sample.html) <br>
- [API Documentation](skills/smyx_analysis/references/api_doc.md) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, JSON, shell commands, guidance] <br>
**Output Format:** [Markdown and JSON analysis reports with structured plant identification details, status text, and report links.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Can save output to a file when an output path is provided.] <br>

## Skill Version(s): <br>
999.999.999 (source: server release metadata; source skill frontmatter reports 1.0.7) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
