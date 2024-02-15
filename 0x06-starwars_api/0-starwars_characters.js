#!/usr/bin/node

const request = require('request');
const process = require('process');

function getMovieCharacters (movieId) {
  const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

  request.get(url, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      process.exit(1);
    }

    if (response.statusCode !== 200) {
      console.error(`Error: code status ${response.statusCode}`);
      process.exit(1);
    }

    const filmData = JSON.parse(body);
    const characterUrls = filmData.characters;

    const characterPromises = characterUrls.map(characterUrl => {
      return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
          if (error) {
            reject(new Error(`Character not found: ${error.message}`));
          } else {
            const characterData = JSON.parse(body);
            resolve(characterData.name);
          }
        });
      });
    });

    Promise.all(characterPromises)
      .then(characterNames => {
        characterNames.forEach(name => {
          console.log(name);
        });
      })
      .catch(error => {
        console.error(`Error: ${error.message}`);
        process.exit(1);
      });
  });
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
