from fastapi import APIRouter

router = APIRouter()

@router.get('/api/v1/personagens')
async def get_cursos():
    return {'info': 'Todos os personagens'}