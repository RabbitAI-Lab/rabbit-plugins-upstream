import {buildScene} from './_film-diagram-scenes-c.mjs';
export const defaults={"milestones":[{"date":"Week 1","caption":"A rough prototype"},{"date":"Week 3","caption":"A small pilot"},{"date":"Week 6","caption":"A public release"}],"presenter":false};
export const meta={"slug":"bs-creatormotion-diagram-timeline-nodes","name":"Timeline Node Reveal","category":"diagram","description":"Reveal milestones in order along a shared horizontal track. Leave a clear settled interval after the final label.","duration":6.6};
// The scene lays the track out per aspect (horizontal in landscape, vertical in portrait) and, when presenter is on,
// places a round picture-in-picture window in the top-right corner framed with ctx.frame.
export default ctx=>buildScene('timeline-nodes',ctx);
