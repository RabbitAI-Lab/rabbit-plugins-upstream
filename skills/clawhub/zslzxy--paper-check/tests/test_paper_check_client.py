from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch


CLIENT_PATH = Path(__file__).resolve().parents[1] / "scripts" / "paper_check_client.py"
SPEC = importlib.util.spec_from_file_location("paper_check_client", CLIENT_PATH)
assert SPEC and SPEC.loader
CLIENT = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CLIENT)


class _Response:
    status = 200

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc, traceback):
        return False


class OssStsUploadTest(unittest.TestCase):
    def test_vip_sts_upload_uses_bucket_virtual_host_like_ali_oss(self):
        ticket = {
            "endpoint": "https://oss-cn-test.aliyuncs.com",
            "bucketName": "paper-bucket",
            "uploadObjectKey": "tmp/order/paper.docx",
            "objectKey": "private/order/paper.docx",
            "accessKeyId": "temporary-id",
            "accessKeySecret": "temporary-secret",
            "securityToken": "temporary-token",
        }

        with patch.object(CLIENT.urllib.request, "urlopen", return_value=_Response()) as urlopen:
            object_key = CLIENT.put_upload(
                CLIENT.Rest(dry_run=False, timeout=5),
                ticket,
                b"fixture",
                "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            )

        request = urlopen.call_args.args[0]
        self.assertEqual(
            request.full_url,
            "https://paper-bucket.oss-cn-test.aliyuncs.com/tmp/order/paper.docx",
        )
        self.assertEqual(object_key, "private/order/paper.docx")


class ReportVerifyRoutingTest(unittest.TestCase):
    def setUp(self):
        self.route = {
            "site": "https://vpcs.cqccjy.cn",
            "owner_user_id": 2,
            "pages": {
                "entry": "https://vpcs.cqccjy.cn/pwp/verify",
                "vip": "https://vpcs.cqccjy.cn/pwp/verify",
                "wanfang": "https://truth.wanfangdata.com.cn/",
                "cnki": "https://check7.cnki.net/codeverify/",
            },
        }

    def test_verify_without_brand_returns_complete_fixed_page_map(self):
        result = CLIENT.envelope("report-verify", "cqccjy", self.route, "verify", None)

        self.assertEqual(result["browser_url"], "https://vpcs.cqccjy.cn/pwp/verify")
        self.assertEqual(result["browser_urls"]["wanfang"], "https://truth.wanfangdata.com.cn/")
        self.assertEqual(result["browser_urls"]["cnki"], "https://check7.cnki.net/codeverify/")

    def test_verify_brand_selects_the_matching_page(self):
        route = CLIENT.verification_route(self.route, "cnki")
        result = CLIENT.envelope("report-verify", "cqccjy", route, "verify", None)

        self.assertEqual(result["browser_url"], "https://vpcs.cqccjy.cn/pwp/verify")
        self.assertEqual(result["browser_urls"]["cnki"], "https://check7.cnki.net/codeverify/")


if __name__ == "__main__":
    unittest.main()
