## Description: <br>
Helps agents simplify JavaScript and TypeScript code by suggesting Licia utility-library functions for common data, type-checking, string, object, array, DOM, date, encoding, and helper patterns. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[surunzi](https://clawhub.ai/user/surunzi) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and coding agents use this skill when writing or reviewing JavaScript/TypeScript to replace hand-written utility logic with appropriate Licia imports and examples. It is useful for refactoring repetitive helper code, data manipulation, type checks, string processing, DOM helpers, and related utility patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may suggest Licia utilities that touch filesystem, process control, URL or file opening, network requests, or raw HTML DOM operations. <br>
Mitigation: Require explicit user intent for those APIs and review each suggested import or replacement before applying it. <br>
Risk: Raw HTML DOM helpers can be unsafe when used with untrusted content. <br>
Mitigation: Prefer safer text APIs or sanitized DOM patterns for untrusted input. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/surunzi/skills/licia) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code] <br>
**Output Format:** [Markdown guidance with JavaScript/TypeScript import examples and replacement snippets] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Review suggestions before accepting imports, especially for filesystem, process-control, URL/file opening, network, and raw HTML DOM APIs.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata and artifact metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
