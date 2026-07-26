## Description: <br>
Deep Scraper uses a containerized Crawlee and Playwright workflow to scrape complex sites such as YouTube and return transcript, description, or generic page content as JSON. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[opsun](https://clawhub.ai/user/opsun) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Developers and agents use Deep Scraper to run a Dockerized browser scraper against public or explicitly authorized web pages, then consume cleaned page text or YouTube transcript and description data as JSON. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Using the scraper on private, internal, authenticated, or otherwise unauthorized pages can create privacy and access-control risks. <br>
Mitigation: Use only on public or explicitly authorized pages, and avoid private/internal URLs and authenticated content. <br>
Risk: The skill runs a Dockerized browser scraper and the security guidance calls out dependency hygiene and Dockerfile review before building. <br>
Mitigation: Review or supply the Dockerfile, update or pin Playwright and Crawlee, and run the container in a controlled environment. <br>


## Reference(s): <br>
- [Deep Scraper on ClawHub](https://clawhub.ai/opsun/skills/deep-scraper) <br>


## Skill Output: <br>
**Output Type(s):** [text, json, code, shell commands, configuration, guidance] <br>
**Output Format:** [JSON emitted to stdout, with setup and usage guidance in Markdown and shell commands] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Scraped text is truncated by the handlers before being returned; YouTube outputs include video ID validation when transcript data is available.] <br>

## Skill Version(s): <br>
1.0.1 (source: server release evidence; package.json declares 1.0.0) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
