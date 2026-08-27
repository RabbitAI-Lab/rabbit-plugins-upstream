import {Audio} from "@remotion/media";
import {AbsoluteFill, Easing, Img, Sequence, interpolate, staticFile, useCurrentFrame} from "remotion";
import script from "../script.json";

type Role = "primary" | "secondary" | "tertiary" | "foreground";
type Layer = {src: string; speaker?: string; role: Role; x: number; y: number; width: number; delay: number; z: number; from: "left" | "right" | "bottom"};
type Speaker = string;
type Narration = {id: string; scene: string; speaker: Speaker; text: string; caption?: string; output: string; from: number; durationInFrames: number};

const motion = {primary: {distance: 78, rise: 55, scale: .86}, secondary: {distance: 58, rise: 38, scale: .9}, tertiary: {distance: 38, rise: 22, scale: .95}, foreground: {distance: 50, rise: 30, scale: .92}};
const filter = "drop-shadow(4px 0 #f5eedc) drop-shadow(-4px 0 #f5eedc) drop-shadow(0 4px #f5eedc) drop-shadow(0 18px 9px rgba(20,15,12,.32))";

const Cutout = ({layer, speaking}: {layer: Layer; speaking: boolean}) => {
  const frame = useCurrentFrame();
  const local = frame - layer.delay;
  const enter = interpolate(local, [0, 14], [0, 1], {easing: Easing.bezier(.16, 1, .3, 1), extrapolateLeft: "clamp", extrapolateRight: "clamp"});
  const setting = motion[layer.role];
  const side = layer.from === "left" ? -1 : layer.from === "right" ? 1 : 0;
  const bob = local > 14 ? Math.sin((local - 14) / 24) * .8 : 0;
  // Keep every cutout solid. Speech should read as a calm conversational micro-motion,
  // never as transparency or a high-frequency shake.
  const talk = speaking ? Math.sin(frame * .18) : 0;
  const talkScale = speaking ? 1.002 + Math.max(0, talk) * .004 : 1;
  const emphasisY = speaking ? -Math.max(0, talk) * .8 : 0;
  return <Img src={staticFile(layer.src)} style={{position: "absolute", left: layer.x, top: layer.y, width: layer.width, zIndex: layer.z, opacity: 1, transformOrigin: "50% 100%", transform: `translate(${side * (1 - enter) * setting.distance}px, ${layer.from === "bottom" ? (1 - enter) * setting.rise + bob + emphasisY : bob + emphasisY}px) scale(${interpolate(enter, [0, 1], [setting.scale, 1]) * talkScale})`, filter: speaking ? filter : `${filter} saturate(.92)`}}/>;
};

const ExplainCard = ({segment, frame}: {segment?: Narration; frame: number}) => {
  if (!segment || segment.speaker !== "narrator") return null;
  const local = frame - segment.from;
  const cards = (script as typeof script & {phrase_cards?: Record<string, string[]>}).phrase_cards || {};
  const words = cards[segment.id] || [];
  if (!words.length) return null;
  const active = Math.min(words.length - 1, Math.floor(Math.max(local, 0) / Math.max(1, segment.durationInFrames / words.length)));
  return <div style={{position: "absolute", zIndex: 15, top: 56, left: 70, right: 70, display: "flex", justifyContent: "center", gap: 18}}>{words.map((word, index) => <div key={word} style={{padding: "13px 24px", borderRadius: 14, background: index === active ? "#ffd772" : "#f8eed7", color: "#14213b", fontFamily: "Arial, sans-serif", fontWeight: 900, fontSize: 30, letterSpacing: 1, transform: `scale(${index === active ? 1.08 : .94})`, boxShadow: "0 8px 0 rgba(20,33,59,.25)"}}>{word}</div>)}</div>;
};

const Scene = ({scene}: {scene: typeof script.scenes[number]}) => {
  const frame = useCurrentFrame();
  const push = interpolate(frame, [0, scene.durationInFrames], [1, 1.012], {extrapolateRight: "clamp"});
  const narration = (script.narration as Narration[]).filter((segment) => segment.scene === scene.id);
  const activeCaption = narration.find((segment) => frame >= segment.from && frame < segment.from + segment.durationInFrames);
  const title = activeCaption?.text || scene.caption.title;
  // The animation is an English-immersion lesson. Chinese translations belong in
  // the post caption or a separate study sheet, never on the in-video dialogue.
  const subtitle = activeCaption ? "" : scene.caption.subtitle;
  const isCover = scene.id === "cover";
  return <AbsoluteFill style={{overflow: "hidden", background: "#201510"}}>
    <Img src={staticFile(scene.background)} style={{width: "100%", height: "100%", objectFit: "cover", scale: push}}/>
    {scene.layers.map((layer) => {
      const speaker = layer.speaker || (layer.src.includes("female") ? "female" : "male");
      return <Cutout key={`${layer.src}-${layer.x}-${layer.y}`} layer={layer as Layer} speaking={activeCaption?.speaker === speaker}/>;
    }) }
    <ExplainCard segment={activeCaption} frame={frame}/>
    {narration.map((segment) => <Sequence key={segment.id} from={segment.from} durationInFrames={segment.durationInFrames}><Audio src={staticFile(segment.output)}/></Sequence>)}
    {title && <div style={isCover ? {position: "absolute", zIndex: 20, left: 72, top: 150, width: 650, padding: "26px 30px", color: "#fbf1db", background: "rgba(18,33,59,.88)", borderRadius: 20, fontFamily: "Arial, sans-serif", textShadow: "0 3px 0 #14213b"} : {position: "absolute", zIndex: 20, bottom: 32, left: 75, right: 75, padding: "13px 28px", textAlign: "center", color: "#fbf1db", background: "rgba(18,33,59,.78)", borderRadius: 16, fontFamily: "Arial, sans-serif", textShadow: "0 3px 0 #14213b"}}><div style={{fontSize: isCover ? 58 : activeCaption ? 42 : 52, lineHeight: 1.05, whiteSpace: "pre-line", fontWeight: 800}}>{title}</div>{subtitle && <div style={{fontSize: isCover ? 28 : 25, marginTop: 14, color: "#ffd772"}}>{subtitle}</div>}</div>}
  </AbsoluteFill>;
};

export const PaperCollageVideo = () => {
  const soundtrack = (script as typeof script & {soundtrack?: string}).soundtrack;
  let offset = 0;
  const scenes = script.scenes.map((scene) => {
    const from = offset;
    offset += scene.durationInFrames;
    return <Sequence key={scene.id} from={from} durationInFrames={scene.durationInFrames}><Scene scene={scene}/></Sequence>;
  });
  return <AbsoluteFill>
    {soundtrack ? <Audio src={staticFile(soundtrack)}/> : null}
    {scenes}
  </AbsoluteFill>;
};
