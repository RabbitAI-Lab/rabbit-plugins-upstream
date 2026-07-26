## Description: <br>
Scrapes the public PTT web BBS interface to fetch boards, categories, articles, comments, push and boo counts, search results, and essence area listings without login. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[nanookai](https://clawhub.ai/user/nanookai) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Developers and agents use this skill to search, crawl, inspect, and summarize public PTT board content, including article metadata, comment streams, and board-level push/boo statistics. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The article command can fetch arbitrary HTTP URLs if a non-PTT URL is supplied. <br>
Mitigation: Review before installing and pass only public ptt.cc article URLs or paths to the article command. <br>
Risk: Scraped output may include raw usernames, timestamps, comments, and copied article text. <br>
Mitigation: Limit redistribution of raw PTT data and avoid reproducing embedded copyrighted works verbatim. <br>
Risk: Large or aggressive crawls can burden a shared community site. <br>
Mitigation: Keep requests limited to public PTT scraping, respect the bundled delay behavior, and avoid aggressive parallel crawling. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/nanookai/skills/ptt-bbs) <br>
- [ClawHub publisher profile](https://clawhub.ai/user/nanookai) <br>
- [PTT public web interface](https://www.ptt.cc) <br>
- [SKILL.md](artifact/SKILL.md) <br>
- [ptt_scraper.py](artifact/scripts/ptt_scraper.py) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with shell commands and JSON-producing Python script output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The bundled scraper prints UTF-8 JSON with ensure_ascii disabled; article and stats commands may include raw PTT metadata, comments, timestamps, usernames, and push/boo totals.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
