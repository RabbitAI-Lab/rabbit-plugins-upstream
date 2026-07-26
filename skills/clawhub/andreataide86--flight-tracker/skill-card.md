## Description: <br>
Automates checks of flight-search websites for one-way MAO to CNF fares and writes JSON plus text summaries for review. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[andreataide86](https://clawhub.ai/user/andreataide86) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users or personal travel planners can use this skill to run PowerShell connectivity checks against flight-search sources for Manaus (MAO) to Belo Horizonte/Confins (CNF) one-way travel dates and review the generated status summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The release claims automated fare monitoring, filtering, cron execution, and WhatsApp reporting, but the security evidence says the artifact mainly performs connectivity checks and does not implement dependable fare extraction or WhatsApp delivery. <br>
Mitigation: Treat results as preliminary source-load status only; configure scheduling and messaging separately and verify fares manually before acting. <br>
Risk: Flight-search sites may block or limit scripted web requests, and JavaScript-heavy pages may load without exposing fare data. <br>
Mitigation: Review generated error/status summaries after each run and use official booking or airline pages to confirm availability and prices. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/andreataide86/skills/flight-tracker) <br>
- [Google Flights query](https://www.google.com/travel/flights?q=flights+from+MAO+to+CNF+on+2026-08-07+oneway&curr=BRL&hl=pt-BR) <br>
- [Skyscanner MAO to CNF query](https://www.skyscanner.com.br/transporte/passagens-aereas/mao/cnf/?adultsv2=1&cabinclass=economy&currency=BRL&ref=home&rtn=0) <br>
- [LATAM Brazil](https://www.latamairlines.com/br/pt) <br>
- [Azul Airlines](https://www.voeazul.com.br/) <br>


## Skill Output: <br>
**Output Type(s):** [Text, JSON, Shell commands, Guidance] <br>
**Output Format:** [PowerShell console text plus JSON and text summary files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [The script reports whether each source loaded or errored; it does not extract verified fares or deliver WhatsApp messages by itself.] <br>

## Skill Version(s): <br>
1.1.1 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
