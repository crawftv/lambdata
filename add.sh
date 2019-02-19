git add setup.py lambdata_crawftv/ClassificationVisualization.py \
    lambdata_crawftv/TopX.py lambdata_crawftv/test.py add.sh .gitignore;
read -p "enter your commit message: " m;
git status;
git commit -m $m;

