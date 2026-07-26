## Description: <br>
Writes, debugs, and reviews PHP across type juggling, arrays, OOP, Composer, PDO, sessions, PHP-FPM, OPcache, PHP 8 features, security, testing, static analysis, and deployment issues. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[ivangdavila](https://clawhub.ai/user/ivangdavila) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and engineers use this skill to write, debug, review, harden, test, and tune PHP applications and runtime configurations. It is especially useful for common PHP failure modes such as silent 500 responses, Composer autoloading errors, PDO binding issues, session locking, PHP-FPM gateway errors, OPcache deploy behavior, and PHP version upgrades. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill may propose Composer commands, php.ini changes, PHP-FPM reloads, preference updates, or other operations that can affect running PHP systems. <br>
Mitigation: Review proposed commands and configuration changes before applying them to production; test in staging or a local reproduction environment where possible. <br>
Risk: Generated PHP guidance can be incorrect if project constraints such as minimum PHP version, framework ownership, extensions, SAPI, or database layer are assumed incorrectly. <br>
Mitigation: Confirm project-specific constraints before applying code or configuration and run the relevant test suite, static analyzer, and syntax checks after changes. <br>


## Reference(s): <br>
- [ClawHub PHP Skill](https://clawhub.ai/ivangdavila/skills/php) <br>
- [PHP Skill Homepage](https://clawic.com/skills/php) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown with PHP code, shell commands, configuration snippets, and review guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May adapt recommendations to stored user preferences for PHP version, SAPI, framework, style, static analysis, test framework, database layer, and platform assumptions.] <br>

## Skill Version(s): <br>
1.0.2 (source: frontmatter and server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
