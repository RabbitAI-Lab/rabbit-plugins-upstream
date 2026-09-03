## Description:

Generates academic footnote citations for Buddhist canon passages from CBETA references or passage text, adding work metadata, publisher details, volume, page, column, and line information.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gouchunlei2-png](https://clawhub.ai/user/gouchunlei2-png)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, students, and agents assisting with Buddhist studies use this skill to turn known CBETA locations or quoted passages into concise academic footnotes and reference text. It is useful when a user needs citation tracing, publisher and publication-year completion, or page-column-line location details for canon passages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill performs CBETA network lookups, so use depends on access to external Buddhist-text services and their current availability.

Mitigation: Use it only where outbound CBETA lookups are acceptable, and review generated citations against the returned source location for important work.

Risk: The optional 中华大藏经定位.py helper can query fo.ancientbooks.cn with a user-provided login cookie, and storing a broad browser cookie in fo_cookie.txt creates a local secret exposure risk.

Mitigation: Prefer the FO_COOKIE environment variable when that helper is required, keep any cookie narrowly scoped and short lived, and avoid writing broad browser cookies to local files.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gouchunlei2-png/skills/dazangjing-xueshu-yinyong)
- [CBETA citation copy format](https://cbeta.org/citation-copy-format)
- [CBETA collection notation](https://cbeta.org/collection-notation)
- [CBETA original edition data format](https://archive.cbeta.org/data-format/zrx.htm)
- [CBETA stable API](https://cbdata.dila.edu.tw/stable)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown or plain text with optional shell command examples and JSON output from helper scripts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Default response is concise two-line citation text; expanded formats, verification URLs, clipboard use, and JSON output are optional when requested.]

## Skill Version(s):

1.3.0 (source: server release evidence; artifact manifest/frontmatter list 1.2.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
