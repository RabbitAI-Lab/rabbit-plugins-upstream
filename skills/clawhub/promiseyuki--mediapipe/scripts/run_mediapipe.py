#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""MediaPipe Vision Skill - unified CLI for ClawHub / OpenClaw agents.

Supports BOTH generations of the MediaPipe Python API:

  landmarks   Legacy solutions API (models bundled, works offline):
              face / hand / pose / holistic
  tasks       Tasks API (Google's recommended API, needs a model file):
              hand_landmarker / pose_landmarker / face_landmarker /
              face_detector / object_detector / image_segmenter

Input can be an image, a video file, or a live webcam stream. Output can be an
annotated image/video, a JSON dump of detections, and/or a CSV of landmarks.

Usage examples:
  # Hand landmarks from an image (legacy API)
  python run_mediapipe.py landmarks --type hand --input hand.jpg --output out.jpg

  # Pose landmarks from a video + CSV dump
  python run_mediapipe.py landmarks --type pose --input pose.mp4 --output out.mp4 --landmark-csv pose.csv

  # Object detection with the Tasks API (download the model first)
  python run_mediapipe.py tasks --type object_detector --model efficientdet_lite0.tflite --input img.jpg --output det.jpg

  # Selfie segmentation (Tasks API)
  python run_mediapipe.py tasks --type image_segmenter --model selfie_segmenter.tflite --input me.jpg --output mask.png

  # Live webcam
  python run_mediapipe.py landmarks --type pose --input webcam
"""

import argparse
import csv
import json
import os
import sys

IMAGE_EXTS = {".jpg", ".jpeg", ".png", ".bmp", ".webp", ".tiff", ".tif"}
VIDEO_EXTS = {".mp4", ".avi", ".mov", ".mkv", ".webm", ".m4v"}

SOLUTION_MODULES = {
    "face": "face_mesh",
    "hand": "hands",
    "pose": "pose",
    "holistic": "holistic",
}

TASK_CREATORS = {
    "hand_landmarker": "HandLandmarker",
    "pose_landmarker": "PoseLandmarker",
    "face_landmarker": "FaceLandmarker",
    "face_detector": "FaceDetector",
    "object_detector": "ObjectDetector",
    "image_segmenter": "ImageSegmenter",
}

TASK_OPTIONS = {
    "hand_landmarker": "HandLandmarkerOptions",
    "pose_landmarker": "PoseLandmarkerOptions",
    "face_landmarker": "FaceLandmarkerOptions",
    "face_detector": "FaceDetectorOptions",
    "object_detector": "ObjectDetectorOptions",
    "image_segmenter": "ImageSegmenterOptions",
}


def ensure_mediapipe():
    try:
        import mediapipe
        return mediapipe
    except ImportError:
        sys.exit(
            "mediapipe is not installed. Install dependencies first:\n"
            "    pip install -r scripts/requirements.txt"
        )


def is_image(path):
    return os.path.splitext(str(path))[1].lower() in IMAGE_EXTS


def is_video(path):
    return os.path.splitext(str(path))[1].lower() in VIDEO_EXTS


def build_parser():
    p = argparse.ArgumentParser(
        prog="run_mediapipe.py",
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    sub = p.add_subparsers(dest="command", required=True)

    lm = sub.add_parser("landmarks", help="Legacy solutions API (bundled models)")
    lm.add_argument("--type", required=True, choices=sorted(SOLUTION_MODULES),
                    help="which MediaPipe solution to run")
    lm.add_argument("--input", required=True,
                    help="path to an image/video file, or the literal 'webcam'")
    lm.add_argument("--output", help="annotated output path (.jpg/.png/.mp4)")
    lm.add_argument("--max-num", type=int, default=2,
                    help="max faces/hands/poses to track (default 2)")
    lm.add_argument("--min-confidence", type=float, default=0.5,
                    help="detection confidence threshold (default 0.5)")
    lm.add_argument("--landmark-csv", help="write per-landmark coordinates to a CSV")
    lm.add_argument("--json", dest="json_out", help="write structured results to a JSON file")
    lm.add_argument("--no-draw", action="store_true", help="disable landmark drawing")
    lm.set_defaults(runner="landmarks")

    tk = sub.add_parser("tasks", help="Tasks API (requires a model file)")
    tk.add_argument("--type", required=True, choices=sorted(TASK_CREATORS))
    tk.add_argument("--model", required=True,
                    help="path to the .task/.tflite model file (see references/api_cheatsheet.md)")
    tk.add_argument("--input", required=True,
                    help="path to an image/video file, or the literal 'webcam'")
    tk.add_argument("--output", help="annotated output path")
    tk.add_argument("--max-num", type=int, default=2)
    tk.add_argument("--min-confidence", type=float, default=0.5)
    tk.add_argument("--json", dest="json_out", help="write structured results to a JSON file")
    tk.add_argument("--no-draw", action="store_true", help="disable annotation drawing")
    tk.set_defaults(runner="tasks")

    return p


class MediaInput:
    """Context manager yielding BGR frames from an image, video, or webcam.

    Each yielded value is (frame, timestamp_ms, is_static). is_static is True
    only for a single image (legacy API should then use static_image_mode=True).
    timestamp_ms is monotonic per frame for video/webcam (the Tasks API VIDEO
    mode requires strictly increasing timestamps).
    """

    def __init__(self, src):
        self.src = str(src).strip()
        self.kind = None
        self.fps = None
        self._cap = None

    def __enter__(self):
        import cv2
        self.cv2 = cv2
        lower = self.src.lower()
        if lower in ("webcam", "camera", "0"):
            self._cap = cv2.VideoCapture(0)
            if not self._cap.isOpened():
                raise SystemExit("Could not open webcam (index 0). Check the camera.")
            self.kind = "webcam"
            self.fps = 30.0
        elif is_image(self.src):
            self.kind = "image"
        elif is_video(self.src):
            self._cap = cv2.VideoCapture(self.src)
            if not self._cap.isOpened():
                raise SystemExit(f"Could not open video: {self.src}")
            self.kind = "video"
            self.fps = self._cap.get(cv2.CAP_PROP_FPS) or 30.0
        else:
            raise SystemExit(
                f"Unrecognized input: {self.src}\n"
                "Use an image/video file path or the literal 'webcam'."
            )
        return self

    def __iter__(self):
        import cv2
        if self.kind == "image":
            img = cv2.imread(self.src)
            if img is None:
                raise SystemExit(f"Could not read image: {self.src}")
            yield img, 0, True
            return
        frame_idx = 0
        while True:
            ok, frame = self._cap.read()
            if not ok:
                break
            ts = int(round(frame_idx * 1000.0 / self.fps))
            yield frame, ts, False
            frame_idx += 1

    def __exit__(self, *exc):
        if self._cap is not None:
            self._cap.release()



class LegacyLandmarks:
    """Wraps mp.solutions face_mesh / hands / pose / holistic (bundled models)."""

    def __init__(self, kind, max_num, min_conf, draw, static):
        self.kind = kind
        self.max_num = max_num
        self.min_conf = min_conf
        self.draw = draw
        self.static = static
        self._last_results = None

    def __enter__(self):
        mp = ensure_mediapipe()
        self.mp = mp
        module = getattr(mp.solutions, SOLUTION_MODULES[self.kind])
        common = {"min_detection_confidence": self.min_conf}
        if self.kind == "face":
            self.solver = module.FaceMesh(
                static_image_mode=self.static, max_num_faces=self.max_num,
                refine_landmarks=True, **common)
            self.names = ("face",)
            self.fields = ("multi_face_landmarks",)
        elif self.kind == "hand":
            self.solver = module.Hands(
                static_image_mode=self.static, max_num_hands=self.max_num,
                min_tracking_confidence=0.5, **common)
            self.names = ("hand",)
            self.fields = ("multi_hand_landmarks",)
        elif self.kind == "pose":
            self.solver = module.Pose(
                static_image_mode=self.static, model_complexity=1,
                min_tracking_confidence=0.5, **common)
            self.names = ("pose",)
            self.fields = ("pose_landmarks",)
        else:  # holistic
            self.solver = module.Holistic(
                static_image_mode=self.static, model_complexity=1,
                min_tracking_confidence=0.5, **common)
            self.names = ("face", "pose", "left_hand", "right_hand")
            self.fields = ("face_landmarks", "pose_landmarks",
                           "left_hand_landmarks", "right_hand_landmarks")
        return self

    def __exit__(self, *exc):
        if getattr(self, "solver", None) is not None:
            self.solver.close()

    def process(self, frame_bgr, timestamp_ms=None):
        import cv2
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        rgb.flags.writeable = False
        self._last_results = self.solver.process(rgb)
        return self.serialize(self._last_results)

    def serialize(self, results):
        records = []
        for name, field in zip(self.names, self.fields):
            lm_lists = getattr(results, field)
            if lm_lists is None:
                continue
            if not isinstance(lm_lists, (list, tuple)):
                lm_lists = [lm_lists]
            for lm_list in lm_lists:
                records.append({
                    "kind": name,
                    "landmarks": [
                        {
                            "x": lm.x, "y": lm.y, "z": lm.z,
                            "visibility": getattr(lm, "visibility", None),
                            "presence": getattr(lm, "presence", None),
                        }
                        for lm in lm_list.landmark
                    ],
                })
        if self.kind == "hand" and getattr(results, "multi_handedness", None):
            labels = results.multi_handedness
            for j, rec in enumerate(records):
                if j < len(labels) and labels[j].classification:
                    rec["label"] = labels[j].classification[0].label
                    rec["score"] = round(float(labels[j].classification[0].score), 4)
        return records


    def annotate(self, frame_bgr, records):
        if not self.draw or not records:
            return frame_bgr
        res = self._last_results
        if res is None:
            return frame_bgr
        mp = self.mp
        drawing = mp.solutions.drawing_utils
        if self.kind == "face" and res.multi_face_landmarks:
            for lm in res.multi_face_landmarks:
                drawing.draw_landmarks(frame_bgr, lm, mp.solutions.face_mesh.FACEMESH_CONTOURS)
        elif self.kind == "hand" and res.multi_hand_landmarks:
            for lm in res.multi_hand_landmarks:
                drawing.draw_landmarks(frame_bgr, lm, mp.solutions.hands.HAND_CONNECTIONS)
        elif self.kind == "pose" and res.pose_landmarks:
            drawing.draw_landmarks(frame_bgr, res.pose_landmarks, mp.solutions.pose.POSE_CONNECTIONS)
        elif self.kind == "holistic":
            if res.face_landmarks:
                drawing.draw_landmarks(frame_bgr, res.face_landmarks,
                                       mp.solutions.face_mesh.FACEMESH_CONTOURS)
            if res.pose_landmarks:
                drawing.draw_landmarks(frame_bgr, res.pose_landmarks,
                                       mp.solutions.pose.POSE_CONNECTIONS)
            if res.left_hand_landmarks:
                drawing.draw_landmarks(frame_bgr, res.left_hand_landmarks,
                                       mp.solutions.hands.HAND_CONNECTIONS)
            if res.right_hand_landmarks:
                drawing.draw_landmarks(frame_bgr, res.right_hand_landmarks,
                                       mp.solutions.hands.HAND_CONNECTIONS)
        return frame_bgr



def to_proto_landmark_list(landmarks):
    """Convert a plain list of NormalizedLandmark to a protobuf landmark list.

    drawing_utils.draw_landmarks expects a NormalizedLandmarkList proto; Tasks
    API results contain plain Python lists, so rebuild the proto before drawing.
    """
    try:
        from mediapipe.framework.formats import landmark_pb2
    except ImportError:
        return None
    proto = landmark_pb2.NormalizedLandmarkList()
    for lm in landmarks:
        proto.landmark.add(x=float(lm.x), y=float(lm.y), z=float(lm.z))
    return proto


class TasksProcessor:
    """Wraps a MediaPipe Tasks API vision task (hand_landmarker, ...)."""

    def __init__(self, kind, model, max_num, min_conf, no_draw, static):
        self.kind = kind
        self.model = model
        self.max_num = max_num
        self.min_conf = min_conf
        self.no_draw = no_draw
        self.static = static
        self._last_results = None
        self.mask = None

    def __enter__(self):
        mp = ensure_mediapipe()
        self.mp = mp
        if not os.path.isfile(self.model):
            raise SystemExit(
                f"Model file not found: {self.model}\n"
                "Download it first — see references/api_cheatsheet.md for URLs."
            )
        from mediapipe.tasks import BaseOptions
        from mediapipe.tasks.python import vision as mp_vision
        self.mp_vision = mp_vision
        opts_cls = getattr(mp_vision, TASK_OPTIONS[self.kind])
        running_mode = (mp_vision.VisionRunningMode.IMAGE if self.static
                        else mp_vision.VisionRunningMode.VIDEO)
        kwargs = {
            "base_options": BaseOptions(model_asset_path=self.model),
            "running_mode": running_mode,
        }
        if self.kind == "hand_landmarker":
            kwargs.update(num_hands=self.max_num,
                          min_hand_detection_confidence=self.min_conf,
                          min_hand_presence_confidence=self.min_conf,
                          min_tracking_confidence=self.min_conf)
        elif self.kind == "pose_landmarker":
            kwargs.update(num_poses=self.max_num,
                          min_pose_detection_confidence=self.min_conf,
                          min_pose_presence_confidence=self.min_conf,
                          min_tracking_confidence=self.min_conf)
        elif self.kind == "face_landmarker":
            kwargs.update(num_faces=self.max_num,
                          min_face_detection_confidence=self.min_conf,
                          min_face_presence_confidence=self.min_conf,
                          min_tracking_confidence=self.min_conf)
        elif self.kind == "face_detector":
            kwargs.update(min_detection_confidence=self.min_conf)
        elif self.kind == "object_detector":
            kwargs.update(score_threshold=self.min_conf)
        elif self.kind == "image_segmenter":
            kwargs.update(output_category_mask=True, output_confidence_masks=False)
        self.landmarker = getattr(mp_vision, TASK_CREATORS[self.kind]).create_from_options(
            opts_cls(**kwargs))
        return self

    def __exit__(self, *exc):
        if getattr(self, "landmarker", None) is not None:
            self.landmarker.close()

    def process(self, frame_bgr, timestamp_ms=0):
        import cv2
        rgb = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2RGB)
        img = self.mp.Image(image_format=self.mp.ImageFormat.SRGB, data=rgb)
        if self.static:
            self._last_results = self.landmarker.detect(img)
        else:
            self._last_results = self.landmarker.detect_for_video(img, int(timestamp_ms))
        return self.serialize(self._last_results)


    def serialize(self, res):
        if self.kind == "image_segmenter":
            mask = None
            if res.category_mask is not None:
                mask = res.category_mask.numpy_view()
                self.mask = mask
            if mask is None:
                return []
            import numpy as np
            counts = np.bincount(mask.ravel()).tolist()
            return [{"kind": "category_mask", "width": mask.shape[1],
                     "height": mask.shape[0], "category_counts": counts}]
        if self.kind in ("face_detector", "object_detector"):
            out = []
            for det in res.detections:
                bb = det.bounding_box
                cats = [{"label": c.category_name, "score": round(float(c.score), 4),
                         "index": c.index} for c in det.categories]
                out.append({"kind": self.kind,
                            "bounding_box": [bb.origin_x, bb.origin_y, bb.width, bb.height],
                            "categories": cats})
            return out
        field, label_field = {
            "hand_landmarker": ("hand_landmarks", "handedness"),
            "pose_landmarker": ("pose_landmarks", None),
            "face_landmarker": ("face_landmarks", None),
        }[self.kind]
        out = []
        lm_lists = getattr(res, field) or []
        for i, lm_list in enumerate(lm_lists):
            rec = {"kind": self.kind,
                   "landmarks": [{"x": lm.x, "y": lm.y, "z": lm.z} for lm in lm_list]}
            if label_field and getattr(res, label_field, None) and i < len(getattr(res, label_field)):
                rec["label"] = getattr(res, label_field)[i].category_name
            out.append(rec)
        return out

    def annotate(self, frame_bgr, records):
        if self.no_draw or not records:
            return frame_bgr
        import cv2
        if self.kind == "image_segmenter":
            return self._annotate_segmentation(frame_bgr)
        if self.kind in ("face_detector", "object_detector"):
            for r in records:
                x, y, w, h = r["bounding_box"]
                label = (r["categories"][0]["label"] if r["categories"] else self.kind)
                score = (r["categories"][0]["score"] if r["categories"] else 0.0)
                cv2.rectangle(frame_bgr, (x, y), (x + w, y + h), (0, 255, 0), 2)
                cv2.putText(frame_bgr, f"{label} {score:.2f}", (x, y - 6),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1, cv2.LINE_AA)
            return frame_bgr
        field = {
            "hand_landmarker": "hand_landmarks",
            "pose_landmarker": "pose_landmarks",
            "face_landmarker": "face_landmarks",
        }[self.kind]
        connections = {
            "hand_landmarker": self.mp.solutions.hands.HAND_CONNECTIONS,
            "pose_landmarker": self.mp.solutions.pose.POSE_CONNECTIONS,
            "face_landmarker": self.mp.solutions.face_mesh.FACEMESH_CONTOURS,
        }[self.kind]
        res = self._last_results
        if res is None:
            return frame_bgr
        drawing = self.mp.solutions.drawing_utils
        for lm_list in getattr(res, field) or []:
            proto = to_proto_landmark_list(lm_list)
            if proto is not None:
                drawing.draw_landmarks(frame_bgr, proto, connections)
        return frame_bgr

    def _annotate_segmentation(self, frame_bgr):
        import cv2
        import numpy as np
        mask = self.mask
        if mask is None:
            return frame_bgr
        if mask.ndim == 3:
            mask = mask[..., 0]
        person = mask > 0
        background = frame_bgr.copy()
        background = (background * 0.35).astype(np.uint8)
        return np.where(person[..., None], frame_bgr, background).astype(np.uint8)



class OutputWriter:
    """Collects annotated frames, JSON frames, and CSV rows from the pipeline."""

    def __init__(self, src_kind, out_path, fps, summary):
        self.src_kind = src_kind
        self.path = out_path
        self.fps = fps
        self.summary = summary
        self.video_writer = None
        self.frames = []
        self.csv_rows = []
        self.frame_index = 0

    def write(self, frame, ts, records, processor):
        if self.path:
            if self.src_kind in ("video", "webcam"):
                if self.video_writer is None:
                    import cv2
                    h, w = frame.shape[:2]
                    self.video_writer = cv2.VideoWriter(
                        self.path, cv2.VideoWriter_fourcc(*"mp4v"), self.fps, (w, h))
                self.video_writer.write(frame)
            elif self.frame_index == 0:
                import cv2
                cv2.imwrite(self.path, frame)
                if getattr(processor, "mask", None) is not None:
                    base, _ = os.path.splitext(self.path)
                    cv2.imwrite(base + "_mask.png", processor.mask)
                    print(f"Raw category mask saved to: {base}_mask.png")
        self.frames.append({"index": self.frame_index, "timestamp_ms": ts,
                            "detections": records})
        for rec in records:
            if "landmarks" not in rec:
                continue
            for i, lm in enumerate(rec["landmarks"]):
                self.csv_rows.append([
                    self.frame_index, ts, rec.get("kind", ""), i,
                    lm.get("x", ""), lm.get("y", ""), lm.get("z", ""),
                    lm.get("visibility", ""), lm.get("presence", ""),
                ])
        self.frame_index += 1

    def finalize(self, args):
        if self.video_writer is not None:
            self.video_writer.release()
        json_path = getattr(args, "json_out", None)
        if json_path:
            payload = dict(self.summary)
            payload["frames"] = self.frames
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, indent=2, ensure_ascii=False)
            print(f"JSON results saved to: {json_path}")
        csv_path = getattr(args, "landmark_csv", None)
        if csv_path and self.csv_rows:
            with open(csv_path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["frame", "kind", "landmark_index",
                                 "x", "y", "z", "visibility", "presence"])
                writer.writerows(self.csv_rows)
            print(f"Landmark CSV saved to: {csv_path}")
        if self.path and self.src_kind in ("image", "video"):
            print(f"Annotated output saved to: {self.path}")
        print(f"Processed {self.frame_index} frame(s), "
              f"{sum(len(f['detections']) for f in self.frames)} detection(s) total.")


def run_pipeline(processor, src, args, summary):
    with OutputWriter(src.kind, getattr(args, "output", None), src.fps, summary) as out:
        for frame, ts, is_static in src:
            records = processor.process(frame, ts)
            frame = processor.annotate(frame, records)
            out.write(frame, ts, records, processor)
        out.finalize(args)


    def __enter__(self):
        return self

    def __exit__(self, *exc):
        return False


def run_landmarks(args):
    with MediaInput(args.input) as src:
        processor = LegacyLandmarks(
            args.type, args.max_num, args.min_confidence,
            not args.no_draw, static=(src.kind == "image"))
        with processor:
            run_pipeline(processor, src, args, {
                "api": "solutions", "task": args.type,
                "model": None, "input": args.input,
            })


def run_tasks(args):
    with MediaInput(args.input) as src:
        processor = TasksProcessor(
            args.type, args.model, args.max_num, args.min_confidence,
            args.no_draw, static=(src.kind == "image"))
        with processor:
            run_pipeline(processor, src, args, {
                "api": "tasks", "task": args.type,
                "model": args.model, "input": args.input,
            })


def main(argv=None):
    args = build_parser().parse_args(argv)
    if args.runner == "landmarks":
        run_landmarks(args)
    else:
        run_tasks(args)


if __name__ == "__main__":
    main()

