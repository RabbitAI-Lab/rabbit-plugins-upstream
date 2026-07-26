## Description: <br>
Query Ile-de-France Mobilites (IDFM) PRIM/Navitia for place resolution, journey planning, and disruption checks for transit routes in Ile-de-France. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[anthonymq](https://clawhub.ai/user/anthonymq) <br>

### License/Terms of Use: <br>


## Use Case: <br>
Developers and transit-focused agents use this skill to call IDFM PRIM/Navitia for place lookup, journey options, and active disruption checks when an IDFM PRIM API key is available. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The --base-url option can send the user's IDFM PRIM API key to a user-specified endpoint if invoked with an untrusted URL. <br>
Mitigation: Use the default PRIM/Navitia endpoint, avoid --base-url unless the destination is fully trusted, and use a dedicated revocable IDFM PRIM API key. <br>


## Reference(s): <br>
- [IDFM PRIM / Navitia quick notes](references/idfm-prim.md) <br>
- [IDFM PRIM Navitia API endpoint](https://prim.iledefrance-mobilites.fr/marketplace/v2/navitia) <br>
- [ClawHub skill page](https://clawhub.ai/anthonymq/skills/idfm-journey-navitia) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, JSON] <br>
**Output Format:** [Markdown guidance with shell commands and optional JSON API output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires IDFM_PRIM_API_KEY; --json returns raw PRIM/Navitia API responses.] <br>

## Skill Version(s): <br>
0.1.0 (source: ClawHub release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
