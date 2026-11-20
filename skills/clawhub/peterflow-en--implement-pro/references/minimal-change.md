# Review a proposed change

| Before adding… | Ask | Evidence to act on |
| --- | --- | --- |
| Neighboring cleanup | Which requested entry point still fails without it? | Follow the call chain. Leave unrelated naming, formatting and prior edits in place. |
| An interface, factory or helper | Which current caller needs another implementation? Do these cases obey the same rule? | Use a direct implementation for a single case. Extract when callers share real behavior or an existing contract requires it. |
| A dependency, setting or mode | What capability is missing today? Who needs the second value? | Prefer established project code and the standard library. Explain a necessary addition and its build or deployment cost. |
| A guard or fallback | Which boundary admits that input? Can this layer recover? | Parse at the boundary. Trust established internal types. Handle specific recoverable errors and propagate the rest. |
| Documentation or comments | What decision would the next reader have to reconstruct? | Capture the business reason, public contract or explicitly requested material. |
| Test infrastructure | If the defect returned, which existing assertion would fail? | Exercise the normal entry point. Add the nearest discriminating case when coverage is missing. |

If your diff has grown beyond the request, compare it to the starting state. Remove only your own unrelated edits. Try a local alternative against the same acceptance criteria before retaining a new mechanism. Trace the first failure in a chain and distinguish a required caller adaptation from a separate issue. If fixing B breaks A, test both together before another edit. Explain the smallest extra change if it crosses the user's boundary.

“Only change X” narrows the remaining work to X. “Stop” means halt writes and report what has changed. On an undo request, establish the requested changes and their ownership before reverting. Check the retained diff against the requirements and the observed behavior.
