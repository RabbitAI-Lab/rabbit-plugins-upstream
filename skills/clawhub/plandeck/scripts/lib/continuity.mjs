// continuity.mjs — resilient facade for journal and snapshot observation points.

import { logArchived, logTransitions } from "./journal.mjs";
import { maybeSnapshot } from "./snapshot.mjs";

/** Observe a successfully built live payload without blocking its primary command. */
export function observe(planDir, cards, { actor } = {}) {
  logTransitions(planDir, cards, { actor });
  maybeSnapshot(planDir);
}

/** Observe cards deliberately moved from the live plan into archive.yaml. */
export function observeArchive(planDir, archivedCards, { actor } = {}) {
  logArchived(planDir, archivedCards, { actor });
}
