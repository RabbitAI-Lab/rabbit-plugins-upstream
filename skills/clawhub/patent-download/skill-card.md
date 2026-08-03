## Description: <br>
A patent PDF batch download tool that helps agents query patent information, download full-text patent PDFs, and export patent files across multiple platforms with Google Patents as the preferred channel. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[cat-xierluo](https://clawhub.ai/user/cat-xierluo) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers, legal operations teams, and patent professionals use this skill to generate commands and guidance for querying patent records, downloading individual or batch patent PDFs, and configuring optional platform credentials. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The wrapper can install unpinned Python packages and a Chromium browser at runtime without explicit opt-in. <br>
Mitigation: Run the skill in an isolated virtual environment, review dependencies before installation, and prefer the documented python cli.py commands after manually installing reviewed dependencies. <br>
Risk: Account-based patent platforms may restrict automated or bulk access under their service terms. <br>
Mitigation: Use account-based platforms only when the platform terms and account permissions allow automated access; prefer the public Google Patents path where it satisfies the task. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/patent-download) <br>
- [Author homepage](https://github.com/cat-xierluo/legal-skills) <br>
- [Platform status](references/platform-status.md) <br>
- [Patent number formats](references/patent-number-formats.md) <br>
- [Examples](references/examples.md) <br>
- [Accounts setup and ToS notes](references/accounts-setup.md) <br>
- [Google Patents](https://patents.google.com) <br>


## Skill Output: <br>
**Output Type(s):** [Shell commands, Configuration instructions, Guidance, Files] <br>
**Output Format:** [Markdown guidance with inline shell commands and downloaded patent PDF files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May require optional platform credentials, reviewed Python dependencies, network access, and browser automation depending on the selected patent source.] <br>

## Skill Version(s): <br>
2.6.0 (source: SKILL.md frontmatter, CHANGELOG, ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
