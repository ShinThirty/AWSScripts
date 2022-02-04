#!/bin/bash
ECR_REGION=$1
ECR_REPO=$2

IMAGES_TO_DELETE=$( aws ecr list-images --region $ECR_REGION --repository-name $ECR_REPO --query 'imageIds[0:100]' --output json )

aws ecr batch-delete-image --region $ECR_REGION --repository-name $ECR_REPO --image-ids "$IMAGES_TO_DELETE" || true
