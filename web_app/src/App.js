import React, { useState } from 'react';
import axios from 'axios';

function MyButton({ handleClick, label }) {
  return (
    <button onClick={handleClick}>
      {label}
    </button>
  );
}

export default function MyApp() {
  const [imageUrl, setImageUrl] = useState('');
  const [peopleCount, setPeopleCount] = useState(null);
  const [file, setFile] = useState(null);

  const fetchNumber = async () => {
    try {
      const response = await axios.get('http://localhost:8000/get-image');
      setPeopleCount(response.data.number);
    } catch (error) {
      console.error('Error fetching the number:', error);
    }
  };

  const handleUrlChange = (event) => {
    setImageUrl(event.target.value);
  };

  const fetchNumberFromUrl = async () => {
    try {
      const response = await axios.get(`http://localhost:8000/get-image-from-url?url=${encodeURIComponent(imageUrl)}`);
      setPeopleCount(response.data.number);
    } catch (error) {
      console.error('Error fetching the number from URL:', error);
    }
  };

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const uploadImage = async () => {
    if (!file) {
      alert('Wybierz zdjęcie!');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    try {
      const response = await axios.post('http://localhost:8000/upload-image', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setPeopleCount(response.data.number);
    } catch (error) {
      console.error('Error uploading the image:', error);
    }
  };

  return (
    <div style={{ textAlign: 'center' }}>
      <h1>Welcome to my app</h1>
      <MyButton handleClick={fetchNumber} label="Liczba ludzi zdjęcie z dysku" />
      <div>
        <input
          type="text"
          value={imageUrl}
          onChange={handleUrlChange}
          placeholder="URL zdjęcia"
        />
        <MyButton handleClick={fetchNumberFromUrl} label="Liczba ludzi URL zdjęcia" />
      </div>
      <div>
        <input type="file" onChange={handleFileChange} />
        <MyButton handleClick={uploadImage} label="Liczba ludzi z przesłanego zdjęcia" />
      </div>
      {peopleCount !== null && <p>Number of people: {peopleCount}</p>}
    </div>
  );
}
