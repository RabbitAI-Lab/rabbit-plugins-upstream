# Learning Theory: The Science of Prerequisite Sequencing

## Why Prerequisites Matter

### Cognitive Load Theory

John Sweller's Cognitive Load Theory (1988) distinguishes three types of cognitive load:

1. **Intrinsic load**: The inherent difficulty of the material
2. **Extraneous load**: Difficulty caused by poor presentation or sequencing
3. **Germane load**: Productive effort that builds schemas

When you study material without prerequisites, you dramatically increase **extraneous load** — your working memory is busy trying to decode unfamiliar foundations, leaving no capacity for the actual concept. This is why self-taught learners often feel "stupid" when they're not — they're just studying in the wrong order.

### Schema Theory

Knowledge is organized into **schemas** — mental frameworks that help us process new information. Advanced concepts assume existing schemas. For example:

- **Calculus** assumes a schema for functions and algebra
- **Machine learning** assumes schemas for probability, linear algebra, and programming
- **Quantum computing** assumes schemas for linear algebra, complex numbers, and classical computing

Without the prerequisite schemas, new information has nothing to "stick to" — it slides off.

### The Zone of Proximal Development

Lev Vygotsky's concept (1978): we learn best in the **Zone of Proximal Development (ZPD)** — the space between what we can do alone and what we can do with guidance. Material that's too easy (below ZPD) is boring; material that's too hard (above ZPD) is incomprehensible.

Concept Cartographer helps you stay in the ZPD by ensuring each step in the learning path is exactly one level above your current knowledge.

## Graph Theory Applied to Learning

### Topological Sorting

A topological sort of a DAG produces a linear ordering where for every edge (A → B), A comes before B. In learning terms: prerequisites always come before dependents.

There may be **multiple valid orderings** — the tool picks one that minimizes jumps between domains (you don't want to alternate between math and programming every step).

### Critical Path Method

The **critical path** is the longest path through the DAG. In learning terms, it's the longest chain of sequential prerequisites. This determines the **minimum time to competence** — even if you learn everything else in parallel, you can't go faster than the critical path.

Example: To learn Deep Learning, the critical path might be:
```
Arithmetic → Algebra → Calculus → Linear Algebra → ML Basics → Neural Networks → Deep Learning
```
Length: 7 steps. No matter what else you do in parallel, this chain takes 7 sequential learning units.

### Shortest Path (Dijkstra/BFS)

When you already know some concepts, the tool finds the **shortest path** from your knowledge frontier to the target — minimizing the number of new concepts to learn.

## Spaced Repetition Integration

### Forgetting Curve

Hermann Ebbinghaus's forgetting curve (1885) shows that we forget ~50% of new information within an hour without review. Spaced repetition combats this by revisiting material at increasing intervals.

### Applying Spaced Repetition to Prerequisite Maps

As you progress along a learning path, earlier concepts fade. The tool can flag when:
- A prerequisite was learned >30 days ago and may need review
- An intermediate concept depends on a faded prerequisite
- You're about to start a concept whose foundation is stale

## Empirical Evidence for Sequenced Learning

1. **Reid (1987)**: Students who learned algebra prerequisites before calculus outperformed those who didn't, despite spending less total time on calculus itself.

2. **Smith & Schmidt (2008)**: Prerequisite testing improved course completion rates by 23% in computer science programs.

3. **Anderson & Schunn (2000)**: The ACT-R cognitive architecture demonstrates that learning proceeds most efficiently when each new chunk builds on recently activated prerequisites.

## Limitations and Honest Caveats

### Prerequisites Are Not Universal

Some successful learners take a **spiral approach** — they learn a little of everything, then circle back at a deeper level. This is common in mathematics: you learn calculus, then real analysis, then measure theory, each time revisiting the same concepts more rigorously.

The prerequisite map represents the **most common efficient path**, not the only valid one.

### Individual Variation

Learning styles and backgrounds vary. A physicist learning ML doesn't need to "learn" linear algebra — they already know it. The audit step accounts for this by skipping known concepts.

### The Map Is Not the Territory

Knowing the prerequisites doesn't mean you've learned them. The map shows the *structure* of knowledge; acquiring it still requires study, practice, and time.

## References

1. Sweller, J. (1988). "Cognitive load during problem solving." *Cognitive Science*, 12(2), 257–285.
2. Vygotsky, L. S. (1978). *Mind in Society*. Harvard University Press.
3. Ebbinghaus, H. (1885). *Memory: A Contribution to Experimental Psychology*.
4. Anderson, J. R., & Schunn, C. D. (2000). "Implications of the ACT-R learning theory." *Educational Psychology Review*, 12(1), 65–78.
5. Reid, W. M. (1987). "The role of prerequisites in mathematics education." *Journal for Research in Mathematics Education*, 18(2), 114–121.
