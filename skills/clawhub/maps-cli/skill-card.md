## Description: <br>
Maps Cli geocodes addresses, searches points of interest, retrieves routes and directions, looks up timezones, and exports CSV from the command line using OpenStreetMap-related services. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[itspremkumar](https://clawhub.ai/user/itspremkumar) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers, field operations teams, and agents use this skill to run location lookups, route checks, nearby-place searches, timezone lookups, and CSV exports without a commercial maps API key. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Location searches, coordinates, routes, and POI areas may be disclosed to public OSM-related services. <br>
Mitigation: Avoid sensitive location inputs unless disclosure to those public services is acceptable. <br>
Risk: Running a downloaded Python CLI can execute local code. <br>
Mitigation: Review the downloaded script and run it in an environment appropriate for command-line tools. <br>
Risk: The included CI verifier may inspect untrusted submissions. <br>
Mitigation: Run CI verification for untrusted inputs only in an isolated sandbox without secrets. <br>


## Reference(s): <br>
- [ClawHub Skill Page](https://clawhub.ai/itspremkumar/skills/maps-cli) <br>
- [maps-cli GitHub Repository](https://github.com/itsPremkumar/maps-cli) <br>
- [OpenStreetMap Nominatim Service](https://nominatim.openstreetmap.org) <br>
- [OSRM Routing Service](https://router.project-osrm.org) <br>
- [Overpass API](https://overpass-api.de/api/interpreter) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell command examples; CLI results may be plain text, JSON, or CSV.] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Location queries are sent to public OSM-related services when the CLI is run.] <br>

## Skill Version(s): <br>
2.0.1 (source: server release evidence; artifact frontmatter reports 2.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
