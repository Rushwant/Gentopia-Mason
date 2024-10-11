from typing import AnyStr
from gentopia.tools.basetool import *
import io
import requests
from PyPDF2 import PdfReader




class PDFReaderArgs(BaseModel):
    url: str = Field(..., description="a url of pdf")


class PDFReader(BaseTool):
    """Tool that adds the capability to read a pdf given its link."""

    name = "pdf_reader"
    description = ("A pdf reader which reads a pdf."
                   "Input should be a pdf url.")

    args_schema: Optional[Type[BaseModel]] = PDFReaderArgs

    def _run(self, url: AnyStr) -> str:
      response = requests.get(url)
      if response.status_code != 200:
        raise Exception("Error- unable to read link")
      preader = PdfReader(io.BytesIO(response.content))
      content = ""
      for i in range(len(preader.pages)):
        content += preader.pages[i].extract_text()
      return content

    async def _arun(self, *args: Any, **kwargs: Any) -> Any:
        raise NotImplementedError


if __name__ == "__main__":
    ans = PDFReader()._run("Attention for transformer")
    print(ans)
