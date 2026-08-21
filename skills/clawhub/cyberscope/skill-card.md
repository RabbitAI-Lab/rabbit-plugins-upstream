## Description:

CyberScope packages a security-hardened Next.js and PostgreSQL search engine for a source-linked reference catalog of 62 documented cyber-operation, surveillance, censorship, and defensive methods for threat intelligence, research, education, and defensive threat modeling.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security analysts, researchers, educators, and defenders use CyberScope to run a local searchable catalog of public cyber-operation, surveillance, censorship, and defensive methods for threat intelligence, education, journalism, and defensive threat modeling.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The local app writes its own PostgreSQL tables and stores search terms.

Mitigation: Run it only against a database you control, review stored search data, and disable or minimize query logging when search terms may be sensitive.

Risk: The security scan notes unauthenticated database seeding and exposed search statistics as review concerns.

Mitigation: Keep the app bound to localhost, or add authentication and protect or remove /api/seed and /api/stats before any shared deployment.

Risk: The catalog describes offensive, surveillance, and censorship techniques that could be misused if expanded into procedures.

Mitigation: Use it as descriptive reference material only and do not add exploit steps, payloads, or instructions for unauthorized access, surveillance, or disruption.

Risk: The security guidance recommends updating flagged dependencies before deployment.

Mitigation: Refresh dependencies and rerun security checks before deploying beyond a local research environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/cyberscope)
- [README.md](README.md)
- [SECURITY.md](SECURITY.md)
- [Catalog seed data](src/lib/seed-data.ts)
- [MITRE ATT&CK Collection tactics](https://attack.mitre.org/tactics/TA0009/)
- [CISA Cyber Threats and Advisories](https://www.cisa.gov/topics/cyber-threats-and-advisories)
- [NIST Cybersecurity](https://www.nist.gov/topics/cybersecurity)
- [EFF NSA Spying](https://www.eff.org/nsa-spying)
- [OWASP Internet of Things](https://owasp.org/www-project-internet-of-things/)
- [SANS Social Engineering in Cybersecurity](https://www.sans.org/blog/social-engineering-in-cybersecurity/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands, configuration notes, and local web/API output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and a local PostgreSQL database; the documented app makes no outbound calls.]

## Skill Version(s):

1.0.0 (source: SKILL.md frontmatter and server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
