document.getElementById("addRoomForm").onsubmit = async function(event) {
    event.preventDefault();
    const fleet = parseInt(document.getElementById("fleet").value);
    const ship = parseInt(document.getElementById("ship").value);
    const bus = parseInt(document.getElementById("bus").value);
    const guest = parseInt(document.getElementById("guest").value);

    try {
        const response = await fetch('/add_room/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ fleet, ship, bus, guest })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to add room');
        }

        const result = await response.json();
        document.getElementById("message").innerText = `Room ${result.room_number} added successfully!`;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
    this.reset();
};

document.getElementById("removeRoomForm").onsubmit = async function(event) {
    event.preventDefault();
    const roomNumber = parseInt(document.getElementById("removeRoomNumber").value);

    try {
        const response = await fetch('/remove_room/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ room_number: roomNumber })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to remove room');
        }

        const result = await response.json();
        document.getElementById("message").innerText = result.message;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
    this.reset();
};

document.getElementById("showEmptyRoomsBtn").onclick = async function() {
    try {
        const response = await fetch('/empty_rooms/');
        const result = await response.json();
        document.getElementById("message").innerText = `Number of empty rooms: ${result.empty_rooms}`;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
};

document.getElementById("sortRoomsBtn").onclick = async function() {
    try {
        const response = await fetch('/sorted_rooms/');
        const result = await response.json();
        document.getElementById("message").innerText = `Sorted Rooms: ${result.sorted_rooms.join(", ")}`;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
};

document.getElementById("findRoomForm").onsubmit = async function(event) {
    event.preventDefault();
    const roomNumber = parseInt(document.getElementById("findRoomNumber").value);

    try {
        const response = await fetch(`/find_room/${roomNumber}`);
        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Room not found');
        }

        const result = await response.json();
        document.getElementById("message").innerText = `Room ${roomNumber} details: ${JSON.stringify(result.room_info)}`;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
    this.reset();
};

document.getElementById("saveDataForm").onsubmit = async function(event) {
    event.preventDefault();
    const fileName = document.getElementById("fileName").value;

    try {
        const response = await fetch('/save/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ file_name: fileName })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to save data');
        }

        const result = await response.json();
        document.getElementById("message").innerText = result.message;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }
    this.reset();
};

document.getElementById("addMultipleRoomsForm").onsubmit = async function(event) {
    event.preventDefault();

    const fleetStart = parseInt(document.getElementById("fleetStart").value);
    const fleetEnd = parseInt(document.getElementById("fleetEnd").value);
    const shipStart = parseInt(document.getElementById("shipStart").value);
    const shipEnd = parseInt(document.getElementById("shipEnd").value);
    const busStart = parseInt(document.getElementById("busStart").value);
    const busEnd = parseInt(document.getElementById("busEnd").value);
    const guestStart = parseInt(document.getElementById("guestStart").value);
    const guestEnd = parseInt(document.getElementById("guestEnd").value);

    try {
        const response = await fetch('/add_multiple_rooms/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                fleet_start: fleetStart,
                fleet_end: fleetEnd,
                ship_start: shipStart,
                ship_end: shipEnd,
                bus_start: busStart,
                bus_end: busEnd,
                guest_start: guestStart,
                guest_end: guestEnd
            })
        });

        if (!response.ok) {
            const error = await response.json();
            throw new Error(error.detail || 'Failed to add multiple rooms');
        }

        const result = await response.json();
        document.getElementById("message").innerText = `Rooms added: ${result.added_rooms.join(", ")}`;
    } catch (error) {
        document.getElementById("message").innerText = `Error: ${error.message}`;
    }

    this.reset();
};

document.getElementById('toggleAddRoomFormBtn').addEventListener('click', function() {
    const form = document.getElementById('addRoomForm');
    form.classList.toggle('hidden');
});

document.getElementById('toggleAddMultipleRoomsFormBtn').addEventListener('click', function() {
    const form = document.getElementById('addMultipleRoomsForm');
    form.classList.toggle('hidden');
});