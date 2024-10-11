from transliterate import to_latin, to_cyrillic
from pydantic import BaseModel, Field


class Text(BaseModel):
    content: str = Field("", title="Matnni kiriting:", max_length=10000)
    
    def toKirill(self):
        self.content = to_cyrillic(self.content)
        
    def toLatin(self):
        self.content = to_latin(self.content)