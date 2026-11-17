const { execSync } = require('child_process');
const path = require('path');
const fs = require('fs');

/**
 * Analyze a video file and extract scene keyframes + metadata.
 * @param {string} videoPath - Absolute path to the video file
 * @param {object} [opts]
 * @param {number} [opts.sceneThreshold=0.4] - ffmpeg scene detection threshold (lower = more scenes)
 * @param {string} [opts.outputDir] - Directory to save extracted frames (default: next to video)
 * @returns {{ scenes: Array<{time: string, frame: string}>, duration: number, width: number, height: number, fps: number, keyframeCount: number }}
 */
function summarize(videoPath, opts = {}) {
  const threshold = opts.sceneThreshold ?? 0.4;
  const absPath = path.resolve(videoPath);

  if (!fs.existsSync(absPath)) {
    throw new Error(`Video not found: ${absPath}`);
  }

  // Step 1: Get video metadata
  const probeCmd = [
    'ffprobe', '-v', 'quiet',
    '-print_format', 'json',
    '-show_format', '-show_streams',
    JSON.stringify(absPath)
  ];
  const probeOut = JSON.parse(execSync(probeCmd.join(' '), { encoding: 'utf8' }));
  const stream = (probeOut.streams || []).find(s => s.codec_type === 'video');
  const duration = parseFloat(probeOut.format?.duration || stream?.duration || 0);
  const width = stream?.width || 0;
  const height = stream?.height || 0;
  const fps = (() => {
    const ratio = (stream?.r_frame_rate || '0/1').split('/');
    return ratio.length === 2 ? (parseInt(ratio[0], 10) / parseInt(ratio[1], 10)) : 0;
  })() || 0;

  // Step 2: Scene detection via ffmpeg
  const outputDir = opts.outputDir || path.dirname(absPath);
  const baseName = path.basename(absPath, path.extname(absPath));
  const framesDir = path.join(outputDir, `${baseName}_keyframes`);

  if (!fs.existsSync(framesDir)) {
    fs.mkdirSync(framesDir, { recursive: true });
  }

  const sceneCmd = [
    'ffmpeg', '-i', JSON.stringify(absPath),
    '-vf', `select='gt(scene,${threshold})',showinfo`,
    '-vsync', 'vfr',
    '-frame_pts', '1',
    '-q:v', '2',
    path.join(framesDir, 'frame-%05d.jpg'),
    '-an', '-y'
  ].join(' ');

  try {
    execSync(sceneCmd, { encoding: 'utf8', stdio: ['pipe', 'pipe', 'pipe'], timeout: 120000 });
  } catch (e) {
    // ffmpeg may exit with non-zero on some truncated streams; that's OK if frames were produced
  }

  // Step 3: Collect extracted keyframes with timestamps
  const frames = fs.readdirSync(framesDir)
    .filter(f => /\.jpg$/i.test(f))
    .sort()
    .map(f => {
      const idx = parseInt(f.match(/(\d+)/)?.[1] || '0', 10);
      return { time: (idx / fps).toFixed(2), frame: path.join(framesDir, f) };
    });

  return {
    scenes: frames,
    duration: parseFloat(duration.toFixed(2)),
    width,
    height,
    fps: parseFloat(fps.toFixed(2)),
    keyframeCount: frames.length
  };
}

module.exports = { summarize };
