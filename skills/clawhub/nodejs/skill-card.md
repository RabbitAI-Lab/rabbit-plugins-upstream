## Description: <br>
Builds, debugs, and hardens Node.js servers, CLIs, and npm packages across async behavior, modules, streams, memory, and process lifecycle issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write, review, debug, test, package, and operate Node.js services, CLIs, libraries, workers, and release scripts. It is intended for Node runtime work, not browser-only JavaScript, TypeScript type-system design, Bun, or Deno. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Persistent preference memory can retain unintended sensitive details or stale Node.js guidance preferences. <br>
Mitigation: Do not store secrets in ~/Clawic/data/nodejs/; review, update, or delete those files when persistent preferences are no longer wanted. <br>
Risk: Generated guidance may include code, shell commands, or configuration changes that affect Node.js runtime behavior. <br>
Mitigation: Review proposed changes before applying them, and test in the target repository or environment before deployment. <br>


## Reference(s): <br>
- [ClawHub NodeJS skill page](https://clawhub.ai/ivangdavila/skills/nodejs) <br>
- [Publisher profile](https://clawhub.ai/user/ivangdavila) <br>
- [Clawic NodeJS skill page](https://clawic.com/skills/nodejs) <br>
- [Setup guide](artifact/setup.md) <br>
- [Security guide](artifact/security.md) <br>
- [Runtime guide](artifact/runtime.md) <br>
- [Production guide](artifact/production.md) <br>
- [Diagnostic commands](artifact/commands.md) <br>


## Skill Output: <br>
**Output Type(s):** [Guidance, Markdown, Code, Shell commands, Configuration] <br>
**Output Format:** [Markdown with inline code and shell command examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May read and update user preference memory under ~/Clawic/data/nodejs/ when the user states persistent Node.js preferences.] <br>

## Skill Version(s): <br>
1.0.4 (source: server release evidence and SKILL.md frontmatter) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
