import {buildScene} from './_film-diagram-scenes-b.mjs';
export const defaults={"problem":"What makes a launch work?","parts":["Audience","Promise","Proof","Channel","Timing"],"question":"Which part needs attention first?"};
export const meta={"slug":"bs-creatormotion-diagram-decompose-scan","name":"Decompose and Scan","category":"diagram","description":"Split a main question into smaller parts, then scan them one at a time. Resolve the scan with a final question or takeaway.","duration":7.2};
export default ctx=>buildScene('decompose-scan',ctx);
