## Description:

Downloads patent PDFs, queries patent information, and batch-exports patent files across multiple platforms, with Google Patents preferred and automatic handling for application and publication number formats.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cat-xierluo](https://clawhub.ai/user/cat-xierluo)

### License/Terms of Use:

MIT

## Use Case:

External users and patent workflow practitioners use this skill to retrieve patent full-text PDFs, look up patent metadata, and batch download patent documents from supported public or account-based patent platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The ClawHub security summary reports that the wrapper can automatically install unpinned packages and a Chromium browser during normal use.

Mitigation: Review dependencies first, use a virtual environment, install dependencies manually, and prefer the documented python cli.py path instead of scripts/patent-download.sh.

Risk: Some download channels use PATENT_* credentials and browser/API automation for account-based patent platforms.

Mitigation: Configure only accounts approved for automated access, review each platform's terms, and limit bulk download volume.

Risk: The skill performs external network requests to patent platforms and writes downloaded files locally.

Mitigation: Run only with patent numbers intended for retrieval and set an explicit output directory with suitable permissions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cat-xierluo/skills/patent-download)
- [Publisher profile](https://clawhub.ai/user/cat-xierluo)
- [Homepage](https://github.com/cat-xierluo/legal-skills)
- [Platform status](references/platform-status.md)
- [Patent number formats](references/patent-number-formats.md)
- [Accounts setup and ToS notes](references/accounts-setup.md)
- [Examples](references/examples.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, files]

**Output Format:** [Markdown guidance with shell command examples and local patent PDF or file outputs.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are driven by user-provided patent numbers; downloaded files are written to the selected output directory.]

## Skill Version(s):

2.7.1 (source: frontmatter, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
