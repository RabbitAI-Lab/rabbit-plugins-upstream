## Description: <br>
Query Ile-de-France Mobilites (IDFM) PRIM/Navitia for Paris and suburbs public transport: place resolution, journey planning, and disruption checks. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anthonymq](https://clawhub.ai/user/anthonymq) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to resolve Ile-de-France transit places, plan public transport journeys, and check active RER or metro disruptions through IDFM PRIM/Navitia. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill can send the user's IDFM PRIM API key to a non-IDFM host if an untrusted --base-url value is used. <br>
Mitigation: Use a dedicated IDFM PRIM API key, keep the default official endpoint, and rotate the key if it may have been sent to a non-IDFM host. <br>
Risk: Live transit results depend on IDFM PRIM/Navitia availability and data freshness. <br>
Mitigation: Treat journey and disruption results as current service data and verify critical travel decisions against official IDFM sources. <br>


## Reference(s): <br>
- [IDFM PRIM / Navitia quick notes](references/idfm-prim.md) <br>
- [Ile-de-France Mobilites PRIM developer portal](https://prim.iledefrance-mobilites.fr/) <br>
- [IDFM PRIM Navitia API base URL](https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [Plain text CLI summaries or raw JSON API responses] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IDFM_PRIM_API_KEY and calls the IDFM PRIM/Navitia service.] <br>

## Skill Version(s): <br>
0.1.6 (source: frontmatter and server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
