import { useEffect, useState, useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import axios from 'axios';
import Layout from '../app/layout';

const Home: React.FC = () => {
  const [videoFile, setVideoFile] = useState<File | null>(null);
  const [style, setStyle] = useState<string>('');
  const [generatedVideo, setGeneratedVideo] = useState<string | null>(null);
  const [loading, setLoading] = useState<boolean>(false);
  const BACKGROUND_URL = "../public/background.jpg";

  const onDrop = useCallback((acceptedFiles: File[]) => {
    setVideoFile(acceptedFiles[0]);
  }, []);
  
  const { getRootProps, getInputProps } = useDropzone({   
    accept: {
    'video/mp4': ['.mp4'],
  }});

  const handleStyleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    setStyle(e.target.value);
  };    

  const handleGenerate = async () => {
    if(videoFile && style) {
      setLoading(true);
      const formData = new FormData();
      formData.append('file', videoFile);
      formData.append('model', style);

      try {
        const response = await axios.post('http://localhost:8000/upload_file', formData, {
          headers: {
            'Content-Type': 'multipart/form-data',
          },
        });
        setGeneratedVideo(response.data["File Path to video"]);
      } catch (error) {
        console.error(error);
      } finally {
        setLoading(false);
      }
    }
  };

  return (
    <>
      <Layout>
        <div style={{ background: `url(${BACKGROUND_URL}) no-repeat center center fixed`, backgroundSize: 'cover', height: '100vh', display: 'flex', flexDirection: 'column', alignItems: 'center', justifyContent: 'center' }}>
          
          <div {...getRootProps()} style={{ border: '2px dashed gray', padding: '20px', margin: '10px', width: '300px', height: '300px', display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
            <input {...getInputProps()} />
            <p>Drag & drop a video here, or click to select a video</p>
          </div>
          
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
            <select onChange={handleStyleChange} style={{ margin: '10px', padding: '10px' }}>
              <option value="" disabled selected>Choose your style</option>
              <option value="cryptopunk">CryptoPunk</option>
              <option value="artistic">Artistic</option>
              <option value="picasso">Picasso</option>
              <option value="sci-fi">Sci-Fi</option>
            </select>
            <button onClick={handleGenerate} style={{ margin: '10px', padding: '10px 20px', backgroundColor: 'blue', color: 'white', border: 'none', borderRadius: '5px' }}>Generate</button>
          </div>

          {loading && <p>Loading...</p>}

          {generatedVideo && (
            <div>
              <video width="320" height="240" controls>
                <source src={generatedVideo} type="video/mp4" />
                Your browser does not support the video tag.
              </video>
              <a href={generatedVideo} download>Download</a>
            </div>
          )}
        </div>
      </Layout>
    </>
  );
};

export default Home;
