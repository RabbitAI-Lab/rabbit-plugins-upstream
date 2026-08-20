---
name: research-gap-finder
description: "Investigate genuine research gaps in the scientific literature. Combines 100 curated resources — gap-identification frameworks (PICO/PICOS, six-type gap taxonomy, five-dimension importance rubric, AHRQ, Robinson, Arksey-O'Malley), AI/citation tools (Litmaps, ResearchRabbit, Connected Papers, Elicit, SciSpace, Consensus, Scite, Inciteful), academic databases, bibliometric mining, and a step-by-step workflow — into one agent-operable method that outputs a classified, importance-ranked, citation-backed gap report with a candidate research question per gap."
version: 1.0.0
categories: [research, knowledge]
topics: [research-gaps, literature-review, systematic-review, citation-analysis, academic-research]
metadata:
  openclaw:
    emoji: "🔍"
    requires:
      bins: ["python3", "curl"]
      apis: ["open scholarly APIs (Semantic Scholar, Crossref, OpenAlex, Europe PMC, PubMed E-utilities, arXiv) are key-free; Elicit, SciSpace, Scite, Dimensions and most citation-mapping tools require user accounts / API keys"]
    network:
      outbound: ["api.semanticscholar.org", "api.crossref.org", "api.openalex.org", "www.ebi.ac.uk", "eutils.ncbi.nlm.nih.gov", "export.arxiv.org", "api.biorxiv.org", "api.medrxiv.org", "api.ssrn.com", "api.elsevier.com", "api.incites.clarivate.com", "litmaps.com", "researchrabbit.ai", "connectedpapers.com", "elicit.com", "scispace.com", "consensus.app", "scite.ai", "inciteful.xyz", "dimensions.ai", "scholar.google.com", "patents.google.com"]
---

# 🔍 research-gap-finder

**Turn a broad topic into a ranked, citation-backed list of genuine research gaps — ready to become research questions.**

This skill operationalizes the field's best gap-identification methods so an AI agent
(or a researcher) can run the full pipeline: collect evidence → map the citation
landscape → run semantic "what is unstudied?" queries → classify each gap → rank its
importance → formulate research questions. Every technique is grounded in the companion
catalog in [`resources.md`](resources.md) (100 curated frameworks, tools, databases, and
techniques).

## Integration reality (read first)

- **Open, key-free APIs** are available for the scholarly core: Semantic Scholar, Crossref,
  OpenAlex, Europe PMC, PubMed E-utilities, arXiv. Prefer these for automated queries.
- **Most citation-mapping tools (Litmaps, ResearchRabbit, Connected Papers, Inciteful) are
  browser-based web apps** without a public programmatic API. The agent should *guide the
  human user* through them step-by-step (or drive them via a browser-automation tool where
  permitted by their terms of service), rather than pretending to "upload references" via
  `curl`.
- **Elicit, SciSpace, Scite, Dimensions, Consensus** require user accounts (some paid) for
  full use; the agent must ask the user to provide access or operate them interactively.
- **AnswerThis and Aveksana** are catalogued as AI research-gap tools; they are interactive
  web tools — verify their current availability before relying on them.

## When to use

- A researcher asks: *"what are the research gaps in X?"*
- A PhD student needs a defensible gap for a proposal or literature-review chapter.
- A lab wants to scan a field for understudied angles before committing resources.
- An agent must produce an evidence-backed "state of the field + open problems" brief.

## ⚙️ Operational Workflow

1. **Define the search horizon** — Draft a broad PICO/PICOS statement (Population, Intervention, Comparison, Outcome, Setting). Record it in Obsidian or Notion as the query template for the whole investigation.
2. **Collect recent systematic reviews** — Search PubMed, Cochrane Library, and Scopus for the 3–5 most recent systematic reviews or meta-analyses on the topic. Export their citation lists to Zotero.
3. **Extract explicit gap cues** — For each review, read the **"Limitations"** and **"Future Directions/Research"** sections. Summarize each stated gap in a matrix with columns *Source, Gap type, Evidence*.
4. **Map citation networks** — Import the reference lists into **Litmaps** and run the **reference-gap method**: spot seminal works the reviews failed to cite. Flag each as a potential reference gap.
5. **Visualize disconnections** — Load the same seed set into **ResearchRabbit** and **Connected Papers**. Identify clusters of papers that are never linked ("citation islands"). Record as citation-disconnection gaps.
6. **Run semantic gap queries** — Use **Elicit** or **Consensus** to ask natural-language questions such as *"What aspects of X have not been studied in Y population?"* Capture the answers plus their supporting citations.
7. **Classify gaps with the six-type taxonomy** — Tag every collected gap (reference, disconnection, semantic, or author-stated) as *evidence, methodological, population, contextual, theoretical, or translational* (see Classify & Rank).
8. **Assess importance** — Score each gap with the five-dimension importance rubric (theoretical, practical, feasibility, novelty, coherence). Enter scores into the matrix.
9. **Cross-validate novelty** — Check Dimensions, Google Scholar, preprints (arXiv/bioRxiv/medRxiv/SSRN) and grant databases (NIH RePORTER, NSF Awards, EU CORDIS). Downgrade gaps already funded or recently published.
10. **Triangulate with external evidence** — Check patent databases and industry reports. A gap already patented or industry-validated loses novelty.
11. **Prioritize and rank** — Sort the matrix by importance score × novelty confirmation. Select the top 3–5 gaps.
12. **Formulate research questions** — Using PICO/PICOS and the AHRQ framework, rewrite each prioritized gap as a clear, answerable research question.

## 🤖 AI Tools Playbook

| Tool | What it reveals | How to use it |
|---|---|---|
| **Litmaps** | Reference gaps; citation-network structure | Upload references → inspect which highly-cited papers are *missing* from the set → explore citation clusters for unlinked regions. |
| **ResearchRabbit** | Citation disconnections | Upload references → visually find disconnected nodes/clusters → follow "related work" trails keyword search would miss. |
| **Connected Papers** | Concept maps of a paper's neighborhood | Search a key paper → inspect the graph for isolated concepts → find related papers outside your keyword set. |
| **Elicit** | Semantic search + summarization + extraction | Ask natural-language questions; it finds papers without exact keyword match and extracts takeaways per question. |
| **SciSpace** | Semantic literature search | Plain-text query → AI analyses abstracts/full-text for similar, relevant work. |
| **Consensus** | What has/hasn't been studied | Ask questions over 200M+ papers → evidence-based answers and gaps. |
| **AnswerThis** | Research-gap detection | Analyses existing literature to flag unexplored areas, contradictions, and knowledge gaps. |
| **Aveksana** | Topic research potential | Calculates research potential as a percentage; compare topics; lock a chosen topic. |
| **Semantic Scholar** | TLDR summaries; citation influence | Find papers with TLDRs and influence scores; get recommendations. |
| **Inciteful** | Citation-network graphs | From one paper build the network, find important papers, and the shortest citation path between two papers. |
| **Scite.ai** | Contradictions | Shows whether citations **support, contradict, or merely mention** — contradictions are gaps. |
| **Dimensions** | Research-landscape mapping | Browse grants, publications, citations, and patents in one place to map the field. |

## 📖 Database Search Strategy

**PubMed / PMC** — Combine keywords with MeSH terms and systematic-review filters; search
`"future research"[Text Word]` / `"further study"[Text Word]` in titles/abstracts; snowball
via PMID and `Cited by`.

**Scopus** — Use citation overview to spot low-citation (understudied) clusters; backward
(References) and forward (Cited by) tracking from seminal papers; prioritize `Review`/`Survey`
types.

**Web of Science** — Topic search + timespan refinement; `Cited References` for backward
tracking; `Related Records` (bibliographic coupling) for adjacent understudied areas.

**Cochrane Library** — Search reviews for "insufficient evidence" / "further research";
cross-reference Joanna Briggs EBP reviews for practice-based gaps.

**ERIC (education)** — Thesaurus descriptors instead of colloquial terms; filter for
meta-analyses; cross-context queries to expose contextual disparities.

**PsycINFO (psychology)** — Thesaurus + Boolean; search "methodological limitation" in
meta-analyses/reviews; find excluded-population gaps via "sample bias" queries.

**IEEE Xplore / ACM DL (CS/engineering)** — Conference-first: search "future work" /
"open problem" in top venues (NeurIPS, CHI, AAAI); survey papers' "remaining challenges".

**Google Scholar** — `"future research"` + recent-years filter; author snowballing via
`Cited by`; "knowledge gap" / "contradictory findings" phrase queries.

**Universal tactics** — forward/backward citation tracking from 3–5 pivotal papers;
snowballing (references → search → repeat); dedicate ~30% of search time to scanning
Limitations/Future-Directions; log everything into the evidence matrix.

## 🧭 Classify & Rank Gaps

### Six-type knowledge-gap taxonomy
| Gap type | What to look for | Flag in matrix |
|---|---|---|
| **Evidence** | No (or only weak) studies for a PICO element/outcome | "evidence missing" |
| **Methodological** | Weak designs, outdated instruments, no controls | "methodology limited" |
| **Population** | Demographic/geographic/severity groups absent | "population X not studied" |
| **Contextual** | Settings/cultures/real-world conditions omitted | "context Y absent" |
| **Theoretical** | No explicit theory, or conflicting explanations | "theory Z not applied / contradictory" |
| **Translational** | Findings not moved to practice/policy/product | "implementation not addressed" |

> Operationally, a gap must be shown to be a *genuine absence* (via thorough searching —
> the four causes of gaps: insufficient/imprecise info, biased info, inconsistent results,
> or wrong-kind-of-information) rather than an artifact of incomplete searching.

### Five-dimension importance rubric (score each 0–3)
| Dimension | Question |
|---|---|
| **Theoretical importance** | Does filling it advance core concepts or resolve contradictions? |
| **Practical importance** | Does it solve a real problem or inform policy/practice? |
| **Feasibility** | Are data, methods, and resources realistically obtainable? |
| **Novelty** | Is it genuinely unstudied (check preprints, trials, grants)? |
| **Coherence** | Is it the logical next step of the field's trajectory? |

Sum the scores (max 15). **13–15** high priority → ready for a proposal; **9–12** medium →
needs feasibility work; **≤8** low → re-evaluate relevance. Require at least a 2 in
*Feasibility* to avoid "interesting but impossible".

### Evidence matrix (the backbone of the pipeline)
| Study (citation) | Design/Method | Population | Setting | Findings | Gap(s) identified |
|---|---|---|---|---|---|
| … | … | … | … | … | … |

> ⚠️ **Gap identification ≠ importance assessment.** Identification ends when the "Gap(s)"
> cell is non-empty. Importance is judged *afterwards* with the rubric. Many gaps are
> genuine but unimportant — never conflate absence of evidence with value of evidence.

## 🚀 Advanced Mining Strategies

- **Patents** — Google Patents, USPTO, Espacenet: what's patented but not academically researched.
- **Preprints** — arXiv, bioRxiv, medRxiv, SSRN: cutting-edge work and emerging gaps before publication.
- **Conference proceedings** — NeurIPS, CHI, AAAI, ACM, IEEE: mine "future work" sections.
- **Theses/dissertations** — ProQuest, OATD, EThOS: PhD authors state gaps explicitly.
- **Grants** — NIH RePORTER, NSF Awards, EU CORDIS: what's funded — and what's not.
- **Clinical trials** — ClinicalTrials.gov, WHO ICTRP: conditions/interventions with few or no trials.
- **Policy & industry** — WHO, World Bank, OECD; McKinsey, Gartner, Deloitte: where policy/industry outpace evidence.
- **Replication & failures** — PLOS ONE, Journal of Articles in Support of the Null Hypothesis: findings that fail to replicate.
- **Cross-disciplinary browsing** — concepts/methods in adjacent fields not yet applied to yours.
- **Bibliometrics** — VOSviewer (co-citation/keyword maps), CiteSpace (burst keywords/trends), Bibliometrix (R), Gephi (network visualization), Publish or Perish (citation metrics).

## 📋 Output: The Gap Report

Document every identified gap with this schema:

- **Gap statement** — a concise, declarative sentence of what's missing.
- **Gap type** — six-type taxonomy label.
- **Source evidence** — the specific papers/reviews/queries that establish the absence.
- **Importance assessment** — five-dimension rubric scores + total.
- **Confidence** — High / Medium / Low, based on source quality and search depth.
- **Candidate research question** — one falsifiable question that would fill the gap.

### Honesty & anti-hallucination rules
1. **Zero-invented citations** — every gap must trace to an identifiable source; otherwise mark it "Exploratory/Hypothetical".
2. **Separate identification from importance** — always run the rubric; never present a trivial absence as valuable.
3. **Label confidence** — AI-assisted semantic findings unverified by a review are capped at Medium.
4. **No invented trends** — if the literature is sparse, say "insufficient literature to determine trends", don't speculate.
5. **Absence ≠ algorithm failure** — a missing paper in Litmaps/ResearchRabbit may be a search artifact; cross-check with the AHRQ framework before calling it a gap.
6. **Verify every citation you output** — resolve DOIs/titles via Crossref or a scholarly API before writing them into the report; never emit a citation you cannot resolve.

## ✅ Quick-Start Checklist

1. Pick 3–5 recent systematic reviews in the area
2. Read every "Limitations" and "Future Directions" section
3. Upload references to Litmaps → find reference gaps
4. Use ResearchRabbit → visualize citation disconnections
5. Use Elicit/Consensus → ask what's unstudied
6. Build the evidence matrix (Study → Method → Population → Findings → Gaps)
7. Classify each gap with the six-type taxonomy
8. Rank gaps with the five-dimension rubric
9. Cross-check grant databases and preprints for novelty
10. Formulate a research question from the most promising gap

## 📚 The 100-Resource Catalog

The complete, categorized reference list this skill is built on — frameworks, AI tools,
databases, strategies, courses, YouTube channels, books, library guides, reference managers,
bibliometric tools, communities, key papers, and advanced mining strategies — lives in
[`resources.md`](resources.md).

---
*Authored with the repo's AI reasoning team (6 models drafting in parallel, 4 reviewing), and published under the Skill Publishing Standard.*
