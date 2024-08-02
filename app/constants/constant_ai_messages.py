TRANSFORM_PLAN_STRING_EDITOR_JS_JSON_MESSAGE = """
Based on the previous travel plan, can you please transform it into JSON data structure 
that editor js can take as input and then render in the editor js UI
For your information, the sample editor JSON data is below:
{
  "blocks": [
    {
      "id": "6PT-SAALjc",
      "type": "header1",
      "data": {
        "text": "Heading 1",
        "level": 1
      }
    },
    {
      "id": "z5cZEev912",
      "type": "header2",
      "data": {
        "text": "Heading 2",
        "level": 2
      }
    },
    {
      "id": "Ap9qqUvd_5",
      "type": "header3",
      "data": {
        "text": "Heading 3",
        "level": 3
      }
    },
    {
      "id": "D1j8dOs6Bi",
      "type": "list",
      "data": {
        "style": "ordered",
        "items": [
          "list1",
          "list2",
          "list3"
        ]
      }
    },
    {
      "id": "t9UKTJ93ZN",
      "type": "image",
      "data": {
        "caption": "image caption",
        "withBorder": false,
        "withBackground": false,
        "stretched": false,
        "file": {
          "url": "https://storage.googleapis.com/travel-go-f77a8.appspot.com/nextjs.png?Expires=1754108458&GoogleAccessId=firebase-adminsdk-5ax28%40travel-go-f77a8.iam.gserviceaccount.com&Signature=vK02QLw7%2F%2BYBIHkahhuii5hm20F2TGHDCrb8Fv2jI90cB0IkTvYH1%2BVgPFGBQzdfRQ%2B%2BibVVR%2BZZr0XjOBM0nucPEPxGIVvesblUkGs67Aoq7ca%2B6Qv91lhmu7jGTGZG5s4hzllPrv1muXRlHNh8OZfxKTRP0a2bP%2BgWF2IfjlqV%2FML9Lmfmq9kduVUtODdUkToyjN9AHJhPOqIUwX0K7Xj762LK3Xld2LvKW5h%2FZAxR%2Fp8hhb%2BNK6TVOgOxqHag3XfvBeqO68iEXExZ%2FSN%2FyP45V2gXJuU8PvCgRGAuIedo6wSUn7wMVCWMAv3tqqP%2FebqNHJj2Rxe6dFYUW%2F8NzQ%3D%3D"
        }
      }
    },
    {
      "id": "-EvjPU_4iw",
      "type": "delimiter",
      "data": {}
    },
    {
      "id": "4pwfpzmZBo",
      "type": "linkTool",
      "data": {
        "link": "https://github.com/codex-team/editor.js/blob/next/docs/tools.md",
        "meta": {
          "title": "editor.js/docs/tools.md at next · codex-team/editor.js · GitHub",
          "description": "A block-style editor with clean JSON output. Contribute to codex-team/editor.js development by creating an account on GitHub."
        }
      }
    },
    {
      "id": "hkZ7e0t8gZ",
      "type": "checklist",
      "data": {
        "items": [
          {
            "text": "checklist1",
            "checked": false
          }
        ]
      }
    },
    {
      "id": "xz_cWWug25",
      "type": "warning",
      "data": {
        "title": "this is warning",
        "message": "warning message"
      }
    }
  ]
}
"""
