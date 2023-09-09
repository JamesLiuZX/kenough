import { useEffect, useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import Layout from '../app/layout';

const Home: React.FC = () => {
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [style, setStyle] = useState<string>('');
  const BACKGROUND_URL = "../public/background.jpg";

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setVideoFile(acceptedFiles[0]);
  }, []);
  
  const { getRootProps, getInputProps } = useDropzone({
    accept: {
      'video/mp4': ['.mp4'],
    }  });

  const handleStyleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setStyle(e.target.value);
  };    

  const handleGenerate = async () => {
    if(videoFile) {
      const formData = new FormData();
      formData.append('video', videoFile);
      formData.append('style', style);

      try {
        const response = await axios.post('/api/endpoint', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        console.log(response.data);
      } catch (error) {
        console.error(error);
      }
    }
  };

  return (
    <>
    <Layout>
      <div style={{ background: `url(${BACKGROUND_URL}) no-repeat center center fixed`, backgroundSize: 'cover', height: '100vh', display: 'flex', flexDirection: 'row', alignItems: 'center', justifyContent: 'center' }}>
        <div {...getRootProps()} style={{ border: '2px dashed gray', padding: '20px', margin: '10px', width: '300px', height: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <input {...getInputProps()} />
          <p>Drag & drop a video here, or click to select a video</p>
        </div>
        <div style={{ marginLeft: '20px' }}>
          <select onChange={handleStyleChange} style={{ margin: '10px', padding: '10px' }}>
            <option value="" disabled selected>Choose your style</option>
            <option value="cryptopunk">CryptoPunk</option>
            <option value="artistic">Artistic</option>
            <option value="picasso">Picasso</option>
            <option value="sci-fi">Sci-Fi</option>
          </select>
          <button onClick={handleGenerate} style={{ margin: '10px', padding: '10px 20px', backgroundColor: 'blue', color: 'white', border: 'none', borderRadius: '5px' }}>Generate</button>
        </div>
      </div>
    </Layout>
    </>
  );
};

export default Home;
