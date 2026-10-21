# JobGenie: Tailored Job Applications at Scale

Your strongest qualification might be something you left off your résumé. JobGenie helps you uncover overlooked capabilities, builds a reusable skills matrix, and researches what each employer needs. It then writes a tailored résumé and cover letter showing how you can do the work, supported by your most relevant experience. Your answers and preferences carry forward, so every application draws on the full picture of what you bring.

## What you get

- Guided career discovery, including related skills, software, tools and contributions your résumé may overlook.
- A reusable career reference and skills matrix that incorporate your answers and corrections.
- Job discovery that searches current openings using your capabilities and preferences, including relevant roles beyond your previous job titles.
- Employer OSINT covering the actual role, compensation, day-to-day work, relevant company projects and problems the hire needs to solve.
- A bespoke résumé and complementary cover letter using your strongest relevant experience.
- Review for persuasive logic, hedging, minimization, readability, AI slop and formatting, followed by corrections and delivery.

One OpenClaw can do all of this. If you have others, you can assign a writer and reviewer in plain language.

## Install

Download [JobGenie 1.0.1 from GitHub Releases](https://github.com/RedRookAI/openclaw-skills/releases/tag/jobgenie-v1.0.1), then extract the ZIP’s `jobgenie` folder into your OpenClaw workspace’s `skills/` directory.

Install from [ClawHub](https://clawhub.ai/redrookai/skills/jobgenie):

```sh
openclaw skills install @redrookai/jobgenie
```

For a manual installation, extract the ZIP's `jobgenie` folder into your OpenClaw workspace's `skills/` directory, keeping its `SKILL.md`, references and scripts together. Use your normal OpenClaw skill-discovery flow. [Official skills documentation](https://docs.openclaw.ai/tools/skills).

## Start with your experience

Tell your Claw:

> Use JobGenie to review my résumé and help me build my career reference and skills matrix. Suggest related skills I may have overlooked and ask questions where useful. Save my answers and corrections for future applications.

Share your résumé or point it to career material already in your workspace. If you have no résumé, JobGenie asks about your work and builds the reference conversationally. You can accept, correct or reject its suggestions, including a whole group at once. Discovery can continue as you remember more; you do not need a complete lifetime inventory before applying.

## Find jobs worth applying for

Tell your Claw:

> Use JobGenie to review my résumé and skills matrix, ask about any missing job-search preferences, and find current openings where I could do the work and bring useful experience. Show me the original listings, practical terms and why each role fits before preparing applications.

JobGenie explores relevant role families, reads actual postings and company information, and returns a sourced shortlist. It saves your preferences and findings for reuse. You can then choose a role or authorize a batch of application packets. If you already have a job in mind, go directly to the application workflow.

## Create an application

Provide a job posting or its text, then say:

> Use JobGenie for this role. Research the company and the job, use my saved career reference, and create a bespoke résumé and cover letter. Give me the finished documents to review. Do not submit anything.

The workflow has five rounds:

1. **Research:** use public search, fetch or browser tools for employer OSINT and the actual JD.
2. **Select:** work out how you can help with the employer's needs and choose the most relevant supporting experience. Plan the résumé separately so it adds useful evidence.
3. **Draft:** write both documents using the saved writing and persuasion research.
4. **Review:** assess the packet from the hiring manager's perspective, then check language and presentation in one consolidated review.
5. **Correct and deliver:** apply the changes and produce the requested text/files.

For multiple jobs, give your Claw the list and agree which batch to work through. It reuses your career reference and feedback while researching and tailoring each application separately. The skill does not create background schedules or automatically submit applications.

## Optional separate reviewer

If you have another connected Claw, say:

> This bot writes; my other bot reviews.

Name the bots in your own setup. The writer performs rounds 1, 2, 3 and 5; the reviewer performs round 4. They use existing connections. A different model family is optional. If the other bot is unreachable, JobGenie offers local review or a handoff you can pass along. On one Claw, review and corrections remain separate rounds.

## Tools, files and saved feedback

JobGenie uses your OpenClaw's configured model and existing public research tools. It requires no JobGenie account, additional model provider, Slack workspace or Google connection. Model and search usage follow your existing setup.

The included DOCX helpers use Python 3's standard library, with no Python packages to install. Python is needed only for those helpers; another existing document tool can be used instead. PDF export and page inspection use whatever suitable tools your environment already has. The Claw reports unavailable formats rather than pretending an export succeeded.

The [formatting guide](references/formatting.md) calls for visible spacing between letter paragraphs and résumé sections, readable typography and natural page flow. The bundled helpers apply those defaults and support completing missing files after an interrupted export while preserving finished documents.

Your career reference, matrix, feedback and application files stay in your working project directory, outside the installed skill. Your configured AI/research tools process material as they normally do; this skill does not add a separate storage or upload service. See the [source and feedback instructions](references/sources.md).

## Research and method

Research is included in the package and connected to the workflow: drafting must read and apply the relevant research text, and review must use the complete bundled Remove AI Slop guide. See [Sources](SOURCES.md) for the primary links and their application, and the [complete five-round method](references/five-round-workflow.md) for the operative instructions.

## Document helper checks

The bundled offline regressions use synthetic candidate data and Python's standard library. They check document text/links, spacing, paragraph grouping, text encoding and recovery; they do not make model calls or establish application-writing quality. From this skill's directory, run:

```sh
python3 -m unittest discover -s tests -v
```

## License

JobGenie's original instructions and helpers are provided under [MIT-0](LICENSE), matching ClawHub's current publication terms. The bundled Remove AI Slop guide retains its [MIT notice](LICENSE-REMOVE-AI-SLOP.txt). Linked research publications remain under their publishers' terms; the package contains research summaries and citations, not full copies of those papers.
