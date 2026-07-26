## Description: <br>
Scraper Template helps developers adapt a Playwright-based template for scraping open-platform API documentation and saving standardized JSON descriptions of modules and interfaces. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[woai36d](https://clawhub.ai/user/woai36d) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers use this skill as a reusable starting point for building platform-specific documentation scrapers. It is intended to extract API menus, endpoint details, request and response parameters, and examples into a consistent local JSON format. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: A derived scraper loads a configured target site in Playwright and saves scraped documentation data locally. <br>
Mitigation: Review the platform-specific subclass, base URL, and output directory before running, and avoid authenticated or sensitive sites unless that capture is intended. <br>
Risk: Template-derived scrapers may extract incomplete or inaccurate API details when site navigation, tables, or dynamic content differ from the expected structure. <br>
Mitigation: Validate the generated JSON against the source documentation before using it for downstream automation or integration work. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/woai36d/skills/scraper-template) <br>


## Skill Output: <br>
**Output Type(s):** [guidance, code, shell commands, configuration, JSON] <br>
**Output Format:** [Markdown guidance with Python code patterns, shell commands, and standardized JSON output examples] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Derived scrapers load target documentation pages with Playwright and write extracted API module data to local JSON files.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
