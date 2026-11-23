<p align="center"><b>Language</b>: English · <a href="./README.zh-CN.md">中文</a></p>

<h1 align="center">yotta-resume · Yuan Jian</h1>

<p align="center">Analyze a resume locally, ask for missing evidence, suggest factual improvements, and export DOCX/PDF.</p>

<p align="center">
  <a href="LICENSE.txt"><img alt="License: MIT" src="https://img.shields.io/badge/license-MIT-blue" /></a>
  <a href="https://www.npmjs.com/package/@yottameta/yotta-resume"><img alt="npm package" src="https://img.shields.io/npm/v/@yottameta/yotta-resume" /></a>
  <a href="https://github.com/YottaMeta/yotta-resume"><img alt="GitHub stars" src="https://img.shields.io/github/stars/YottaMeta/yotta-resume" /></a>
</p>

## What it is

yotta-resume is a job-seeker resume analysis and export tool. It reads Markdown,
UTF-8 text, DOCX, and text-layer PDF resumes, detects an industry from visible resume
content, identifies sections, experience bullets, metrics, contact information, and
JD keyword gaps, then returns high-value questions and improvement suggestions.
After the job seeker confirms the facts, the same resume can be exported to DOCX,
HTML, or PDF.

The core analyzer uses the Python standard library. It makes no network requests,
does not submit resumes, and never invents experience or numbers. PDF input uses
local PyMuPDF and fails clearly when the dependency is missing or the file cannot
be parsed.

## When to use

- Review resume structure, evidence, and measurable outcomes.
- Compare a resume with a target job description.
- Prepare focused follow-up questions for missing facts.
- Run a deterministic, evidence-driven single-round mock interview and review.
- Export a confirmed resume as DOCX/PDF.

**Do not use it** to submit applications, fabricate experience, predict interviews or offers, evaluate protected personal attributes, or create complex design portfolios.

## Quick usage

```bash
# Run doctor, analysis, and next-step guidance in one command
python scripts/yotta_resume.py quickstart --resume resume.md --jd jd.txt

# Check the installed package and optional PDF capabilities
python scripts/yotta_resume.py doctor

# Analyze a resume and print a Markdown report
python scripts/yotta_resume.py audit --resume resume.md

# Analyze a text-layer PDF directly
python scripts/yotta_resume.py audit --resume resume.pdf

# Analyze pasted text or an unsupported legacy document after copying its text
python scripts/yotta_resume.py audit --resume-text - < resume.txt

# Analyze with a JD and output JSON
python scripts/yotta_resume.py audit --resume resume.md --jd jd.txt --format json

# Start a local single-round interview
python scripts/yotta_resume.py interview start --resume resume.md --jd jd.txt \
  --role-family soc --level mid --session interview-session.json

# Non-security industries automatically use the generic role family
python scripts/yotta_resume.py interview start --resume software.md \
  --session software-session.json

# Record an answer, then review the evidence gaps
python scripts/yotta_resume.py interview answer --session interview-session.json --answer answer.md
python scripts/yotta_resume.py interview review --session interview-session.json

# Export DOCX, HTML, and PDF
python scripts/yotta_resume.py export --input revised.md --docx revised.docx --html revised.html --pdf revised.pdf

# Validate role, question-bank, source, ledger, and dual-role contracts offline
python scripts/yotta_resume.py contracts --format json
```

PDF export requires a local Chromium, Chrome, or Edge browser. PDF input requires
`pip install pymupdf`. PDF export uses an isolated browser profile and bounded
retries. Missing browsers, missing PDF dependencies, encrypted files,
and image-only PDFs fail clearly instead of producing a misleading result.
Multi-format export renders into a temporary area and commits only after every
requested format succeeds, so a failed PDF does not leave new DOCX/HTML partial files.

The interview command uses resume findings, explicit JD gaps, and the versioned
question bank. Non-security industries automatically use the `generic` role family;
ambiguous industry signals still require explicit confirmation. It keeps state only in the session file you explicitly pass,
supports interruption and resume, and never writes long-term memory. Answers are
labelled as sufficient, partial, or missing evidence; the review does not produce
an interview score, pass probability, or hiring recommendation.

The `readiness.score` field is a structural rule score only. It is not a recruiter
score. When no JD is provided, job-match coverage is `null`. JD matching uses a
versioned fixed vocabulary and reports its limitations; it is not semantic matching
or a hiring recommendation.

Industry detection uses a versioned registry. The bundled bank has 189 items:
six cybersecurity role families with 27 items each and one generic role family
with 27 items. Future industries can be added by extending
`data/industry-registry.json` and its schema without changing the main analysis flow.

See [references/usage.md](references/usage.md) for input format, fields, and exit codes.
See [references/faq.md](references/faq.md) for common questions.
See [references/data-contracts.md](references/data-contracts.md) for the bundled data contracts.
See [examples/software-engineer.example.md](examples/software-engineer.example.md)
and [examples/export-samples](examples/export-samples/) for non-security input and
rendered DOCX / HTML / PDF samples.

## Installation

Choose one of the methods below. Skill files are distributed through **npm**; GitHub hosts source code and issues.

### Method 1: npm one-liner (recommended)

```text
npx -y @yottameta/yotta-resume --agent <agent-name>
npx -y @yottameta/yotta-resume --dir <agent-skills-dir>
```

- `--agent <name>` installs to that agent's default user-level skills directory.
- `--dir <path>` installs to a specified skills directory.
- `--list` shows supported agent defaults.
- If a China mirror has not synced the package, append `--registry=https://registry.npmjs.org/`.

### Method 2: git clone

```text
git clone https://github.com/YottaMeta/yotta-resume.git <agent-skills-dir>/yotta-resume
```

### Method 3: Download ZIP

Download the ZIP from `YottaMeta/yotta-resume`, then move the `yotta-resume` folder into your agent skills directory.

### Method 4: install.sh

```text
bash install.sh --agent <agent-name>
bash install.sh --dir <skills-dir>
bash install.sh --list
```

## Validation

Run `python scripts/yotta_resume.py doctor` after installation. It checks the bundled
contracts, required files, optional PDF backends, browser availability, temporary
directory access, and Python version. Full development tests live in the source
repository and are not required to use the installed skill.

## License

MIT © YottaMeta — see [LICENSE](./LICENSE.txt).
