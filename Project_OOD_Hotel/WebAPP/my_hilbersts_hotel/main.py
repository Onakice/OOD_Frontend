from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel

# นำเข้าคลาส HilbertsHotel ของคุณ
from HilbertsHotel import HilbertsHotel  # แก้ไขเป็นโมดูลที่คุณมี

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

hotel = HilbertsHotel()

# กำหนด Pydantic model สำหรับข้อมูลห้อง
class Room(BaseModel):
    fleet: int
    ship: int
    bus: int
    guest: int

class RoomNumber(BaseModel):
    room_number: int

class FileName(BaseModel):
    file_name: str

# โมเดลสำหรับการเพิ่มห้องหลายห้อง
class MultipleRooms(BaseModel):
    fleet_start: int
    fleet_end: int
    ship_start: int
    ship_end: int
    bus_start: int
    bus_end: int
    guest_start: int
    guest_end: int

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/add_room/")
async def add_room(room: Room):
    room_number = hotel.add_room(room.fleet, room.ship, room.bus, room.guest)
    return {"room_number": room_number}

@app.post("/remove_room/")
async def remove_room(room: RoomNumber):
    hotel.remove_room(room.room_number)
    return {"message": f"Room {room.room_number} removed successfully"}

@app.get("/sorted_rooms/")
async def get_sorted_rooms():
    sorted_rooms = hotel.sort_rooms()
    return {"sorted_rooms": sorted_rooms}

@app.get("/empty_rooms/")
async def get_empty_rooms():
    empty_count = hotel.empty_rooms()
    return {"empty_rooms": empty_count}

@app.get("/find_room/{room_number}")
async def find_room(room_number: int):
    room_info = hotel.find_room(room_number)
    if room_info is None:
        raise HTTPException(status_code=404, detail="Room not found")
    return {"room_info": room_info}

@app.post("/save/")
async def save_data(file: FileName):
    hotel.save_to_file(file.file_name)
    return {"message": "Data saved successfully"}

# เพิ่มฟังก์ชันการเพิ่มห้องหลายห้อง
@app.post("/add_multiple_rooms/")
async def add_multiple_rooms(data: MultipleRooms):
    added_rooms = []
    
    for fleet in range(data.fleet_start, data.fleet_end + 1):
        for ship in range(data.ship_start, data.ship_end + 1):
            for bus in range(data.bus_start, data.bus_end + 1):
                for guest in range(data.guest_start, data.guest_end + 1):
                    room_number = hotel.add_room(fleet, ship, bus, guest)
                    added_rooms.append(room_number)

    return {"added_rooms": added_rooms}

# รันเซิร์ฟเวอร์
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
