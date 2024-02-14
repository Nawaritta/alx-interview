#!/usr/bin/node

const axios = require('axios');
const process = require('process');

function getMovieCharacters(movieId) {
    const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

    axios.get(url)
        .then(response => {
            const characters = response.data.characters;
            const characterPromises = characters.map(characterUrl => {
                return axios.get(characterUrl)
                    .then(response => response.data.name)
                    .catch(error => `Not found`);
            });

            return Promise.all(characterPromises);
        })
        .then(characterNames => {
            characterNames.forEach(name => {
                console.log(name);
            });
        })
        .catch(error => {
            console.log(`Not found`);
        });
}

const movieId = process.argv[2];
getMovieCharacters(movieId);
