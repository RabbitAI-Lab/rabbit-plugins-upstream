## Description: <br>
Iran Chemical Database — an HTTrack-powered live crawling system that autonomously discovers Iranian chemical suppliers, mirrors their websites with HTTrack (with Playwright fallback for JavaScript sites), extracts research-grade molecule catalogs from the local mirrors, validates molecules with RDKit/PubChem, and maintains a live PostgreSQL database served by FastAPI (REST) and Streamlit (dashboard), with Celery scheduling and Docker deployment. Ships complete, runnable source code: discovery engine, HTTrack wrapper, local-file parsers (HTML/PDF/Excel), strict research-grade classifier (English + Persian), live sync, API, dashboard, tests, and docs. For academic procurement research. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Researchers, lab managers, and procurement staff use this skill to build and maintain a live, searchable database of research-grade chemical molecules offered by Iranian suppliers — automatically discovered and kept up to date via HTTrack website mirrors — for sourcing, price comparison, and catalog analysis. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The system crawls third-party websites, which may violate their terms of service or robots.txt if misconfigured. <br>
Mitigation: Polite crawling defaults (robots.txt respected, rate limits, identifiable User-Agent), per-supplier overrides, and explicit legal guidance to mirror only authorized sites. <br>
Risk: Extracted chemical data (grades, purities, prices, GHS) can be inaccurate. <br>
Mitigation: Every record is validated (CAS checksum, RDKit structure, PubChem cross-reference) and flagged with extraction confidence; users must verify before relying on it. <br>
Risk: Requires system services (PostgreSQL, Redis) and, for crawling, the httrack binary and outbound network access. <br>
Mitigation: Full Docker Compose deployment with persistent volumes and a clearly documented environment contract. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/iran-chem-database) <br>
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw) <br>
- [Architecture](docs/architecture.md) <br>
- [HTTrack integration guide](docs/httrack_integration.md) <br>
- [API reference](docs/api_reference.md) <br>
- [Deployment guide](docs/deployment_guide.md) <br>


## Skill Output: <br>
**Output Type(s):** [code, python, sql, yaml, dockerfile, markdown] <br>
**Output Format:** [A complete, runnable Python application (source tree, Docker Compose, migrations, tests, fixtures, docs) implementing the HTTrack-powered crawling database] <br>
**Output Parameters:** [2D] <br>
**Other Properties Related to Output:** [The system writes mirrored websites to a local directory and populates a PostgreSQL database; it makes outbound HTTP requests only to the supplier sites it is configured to mirror.] <br>

## Skill Version(s): <br>
2.3.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, mirror only websites they are authorized to archive, respect robots.txt and site terms of service, verify all extracted chemical data before relying on it, and comply with applicable data/procurement regulations. <br>
